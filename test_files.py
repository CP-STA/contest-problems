from ast import parse
import pytest
import os
import re
import json
import math
from utils import parse_subtask_score


@pytest.fixture(scope="session")
def dir(pytestconfig):
    return pytestconfig.getoption("dir")

def test_path_space(dir):
  _, tail = os.path.split(dir)
  if re.search(r'[^a-z0-9\-]', tail):
    raise ValueError("problem directory contains forbidden character (only letters, numbers, _ and . are allowed).")

def test_files_exist(dir):
  files = os.listdir(dir) 
  for required in ['statement.md', 'test-cases.json', 'constraints.json']:
    if required not in files:
      raise ValueError(f"{required} not found")

@pytest.mark.depends(on=['test_files_exist'])
def test_test_cases_have_components(dir):
  with open(os.path.join(dir, 'test-cases.json')) as f:
    test_cases = json.load(f)
    required_components = [
      'input',
      'output',
    ]
    missing_components = []
    for i, test_case in enumerate(test_cases):
      missing_components_i = []
      for required_component in required_components:
        if required_component not in test_case:
          missing_components_i.append(required_component)
      if missing_components_i:
        missing_components.append([i, missing_components_i])
    if missing_components:
      raise ValueError(f"Some test cases are missing components (required: {required_components}), these are (format: [[test_case_number, [missing_component, ...]], ...]) {missing_components}")

@pytest.mark.depends(on=['test_files_exist', 'test_test_cases_have_components'])
def test_input_white_space(dir):
  with open(os.path.join(dir, 'test-cases.json')) as f:
    test_cases = json.load(f)
    failed_test_cases = []
    for i, test_case in enumerate(test_cases):
      input = test_case['input']
      if re.search("\\s{2,}", input):
        failed_test_cases.append(i)
    if failed_test_cases:
      raise ValueError(f"Multiple consecutive whitespaces detected at input test case number (0 indexed) {failed_test_cases}")

def test_markdown_file_exist(dir):
  files = os.listdir(dir)
  if not 'statement.md' in files:
    raise ValueError(f'statement.md not found')

@pytest.mark.depends(on=['test_markdown_file_exist'])
def test_markdown_has_name(dir):
  with open(os.path.join(dir, 'statement.md')) as f:
    for line in f:
      if line.strip():
        if not line.startswith('# '):
          raise ValueError(f"The markdown does not appear to have any title on the first line. The title should be formatted as `# Problem Title` (note the space) but the first line we found is `{line}`")
        else:
          return
 
@pytest.mark.depends(on=['test_markdown_file_exist'])
def test_markdown_headings_exist(dir):
  should_exists_headings = {
    "Author",
    "Time (ms)",
    "Memory (kb)",
    "Difficulty", 
    "Tags", 
    "Problem Statement",
    "Constraints",
    "Input",
    "Output",
    "Examples",
  }
  not_found_headings = should_exists_headings.copy()
  with open(os.path.join(dir, 'statement.md')) as f:
    for line in f:
      if line.startswith("##") and line[2:].strip() in should_exists_headings:
        not_found_headings.remove(line[2:].strip())
    if not_found_headings:
      raise ValueError(f"Some markdown headings are not found, these are {not_found_headings}. Note that the headings are case sensitive")

@pytest.mark.depends(on=['test_markdown_file_exist'])
def test_markdown_headings_in_order(dir):
  should_exists_headings = [
    "Author",
    "Time (ms)",
    "Memory (kb)",
    "Difficulty", 
    "Tags",
    "Problem Statement",
    "Constraints",
    "Input",
    "Output",
    "Examples",
  ]
  headings_order = []
  with open(os.path.join(dir, 'statement.md')) as f:
    for line in f:
      if line.startswith("##") and line[2:].strip() in should_exists_headings:
        headings_order.append(line[2:].strip()) 
  if headings_order != should_exists_headings:
    raise ValueError(f"Headings in the markdown are not in order, it should be {should_exists_headings}, but found {headings_order}")


def subtasks_count(dir):
  count = 0
  with open(os.path.join(dir, 'statement.md')) as f:
    for line in f:
      if line.startswith("###") and line [3:].strip().split()[0] == "Subtask":
        count += 1
  return count

@pytest.mark.depends(on=['test_markdown_file_exist'])
def test_markdown_tags_parsable(dir):
  with open(os.path.join(dir, 'statement.md')) as f:
    watch = False
    active_lines = []
    for line in f:
      if line.startswith('## '):
        heading = line[2:].strip()
        if heading == 'Tags':
          watch = True
        else:
          watch = False
      elif watch:
        active_lines.append(line)
    tags = list(filter(lambda x: bool(x), list(map(lambda x: x.strip(), ''.join(active_lines).split(',')))))
    for tag in tags:
      if re.search(r'[^a-z0-9 ]', tag):
        raise ValueError(f'We parsed a tag `{tag}`, but only lower case english letter and numbers are allowed. All the tags we parsed are {tags}.')
      
@pytest.mark.depends(on=['test_markdown_file_exist'])
def test_markdown_subtasks(dir):
  if subtasks_count(dir):
    with open(os.path.join(dir, 'statement.md')) as f:
      l2_heading = ''
      numbers_found = []
      numbers_should = list(range(1, subtasks_count(dir) + 1))
      for line in f:
        if line.startswith("## "):
          l2_heading = line[2:].strip()
        if line.startswith("### ") and line[3:].strip().split()[0] == "Subtask":
          if l2_heading != "Constraints":
            raise ValueError(f"Subtasks need to under the heading `Constraints`, currently it's under `{l2_heading}`")
          numbers_found.append(int(line[3:].strip().split()[1]))
      if numbers_found != numbers_should:
        raise ValueError(f"Subtasks incorrectly numbered, expected {numbers_should}, found {numbers_found}.")  

@pytest.mark.depends(on=['test_markdown_file_exist', 'test_markdown_subtasks'])
def test_markdown_subtasks_sum_one(dir):
  if subtasks_count(dir):
    with open(os.path.join(dir, 'statement.md')) as f:
      marks_found = []
      for line in f:
        if line.startswith("###") and line[3:].strip().split()[0] == "Subtask":
          marks_found.append(parse_subtask_score(line))
      found = sum(marks_found)
      if not math.isclose(1, found):
        raise ValueError(f"The sum of all the subtask is not 1 (found the marks to be {marks_found}).")

@pytest.mark.depends(on=['test_markdown_file_exist'])
def test_markdown_example_format(dir):
  with open(os.path.join(dir, 'statement.md')) as f:
    watch = False
    active_lines = []
    for line in f:
      if line.startswith('## '):
        heading = line[2:].strip()
        if heading == 'Examples':
          watch = True
        else:
          watch = False
      elif watch:
        active_lines.append(line)
    ## TODO: parse the example files

    examples = []
    for line in active_lines:
      if line.startswith("### "):
        heading = line[3:].strip()
        examples.append([heading, []])
      elif line.strip() and examples:
        examples[-1][1].append(line)
      elif line.strip():
        raise ValueError(f"The first line under the example heading is not `### Input`. We found `{line}`.")
    
    if len(examples) % 2 != 0:
      raise ValueError("There should be an even number of headings (Input, Output alternating, but we only detected odd number of them")
    for i, example in enumerate(examples):
      if i % 2 == 0:
        if example[0] != "Input":
          raise ValueError(f"Failed to parse the examples. The {i}'th heading is supposed to be `Input` but we found `{example}.")
      else:
        if example[0] != "Output":
          raise ValueError(f"Failed to parse the examples. The {i}'th heading is supposed to be `Output` but we found `{example}.")
      content = ''.join(example[1]).strip()
      if not re.match(r"^```\s*\n[\s\S]*\n```$", content) and not re.match(r"^```\s*\n```$", content):
        raise ValueError(f"Code block not formatted correctly. Found {repr(content)}.")
      

@pytest.mark.depends(on=['test_files_exist'])
def test_json_subtasks_marked(dir):
  if subtasks_count(dir):
    subtasks_found = {}
    missing_test_cases = []
    subtasks_should = set(range(1, subtasks_count(dir)))
    with open(os.path.join(dir, 'test-cases.json')) as f:
      test_cases = json.load(f)
    for i, test_case in enumerate(test_cases):
      if 'subtask' not in test_case:
        missing_test_cases.append(i)
    if missing_test_cases:
      raise ValueError(f"Some test cases are found to not have subtask marked, they are (0 indexed) {missing_test_cases}")

@pytest.mark.depends(on=['test_files_exist'])
def test_json_subtasks_numbered_in_range(dir):
  if subtasks_count(dir):
    subtasks_should = set(range(1, subtasks_count(dir) + 1))
    subtasks_out_range = []
    with open(os.path.join(dir, 'test-cases.json')) as f:
      test_cases = json.load(f)
    for i, test_case in enumerate(test_cases):
      if 'subtask' in test_case and test_case['subtask'] not in subtasks_should:
        subtasks_out_range.append(i)
    if subtasks_out_range:
      raise ValueError(f"The subtask number of some test cases is out of range (expected {subtasks_should}), they are (0 indexed) {subtasks_out_range}")

@pytest.mark.depends(on=['test_files_exist'])
def test_json_less_than_200(dir):
  with open(os.path.join(dir, 'test-cases.json')) as f:
    test_cases = json.load(f)
  if len(test_cases) > 200:
    raise ValueError("Because of a bug on the executioner, it currently does not support more than 200 test cases. We are working on to fix the bug.")

@pytest.mark.depends(on=['test_files_exist']) 
def test_json_subtasks_numbered_all(dir):
  if subtasks_count(dir):
    subtasks_should = set(range(1, subtasks_count(dir) + 1))
    subtasks_found = set()
    with open(os.path.join(dir, 'test-cases.json')) as f:
      test_cases = json.load(f)
    for i, test_case in enumerate(test_cases):
      if 'subtask' in test_case:
        subtasks_found.add(test_case['subtask'])
    if subtasks_should != subtasks_found:
      raise ValueError(f"Not all subtasks numbers are found in the test cases. Expected: {subtasks_should}, found: {subtasks_found}")

@pytest.mark.depends(on=['test_files_exist'])
def test_constraints_exist(dir):
  constraints_expected = {'memory', 'time'}
  constraints_missing = set()
  with open('constraints.json') as f:
    constraints_found = json.load(f)
  for constrain_expected in constraints_expected:
    if constrain_expected not in constraints_found:
      constraints_missing.add(constrain_expected)
  if constraints_missing:
    raise ValueError(f"Some required constraints not found in constraints.json. Those are {constraints_missing}")

@pytest.mark.depends(on=['test_files_exist'])
def test_constraints_same(dir):
  table = {
    "Memory (kb)": "memory",
    "Time (ms)": "time",
  }
  with open('constraints.json') as f:
    constraints = json.load(f)
  diff = []
  with open('statement.md') as f:
    read_next = None
    for line in f:
      if read_next and line.strip():
        number = int(line.strip())
        if number != constraints[read_next]:
          diff.append([read_next, constraints[read_next], number])
        read_next = None
      elif not read_next and table.get(line[2:].strip(), None) in constraints:
        read_next = table.get(line[2:].strip(), None)
    if diff:
      raise ValueError(f"The constraints given in statement.md does not match those given in constraints.json. Difference (format: [[name, number in constraints.json, number in statement.md], ...]): {diff}")
