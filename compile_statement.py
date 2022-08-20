#!/usr/bin/env python

import os
import sys

# If this is python2, check if python3 is available and re-execute with that
# interpreter.
if sys.version_info.major < 3:
  try:
    # On Windows, `py -3` sometimes works.
    # Try this first, because 'python3' sometimes tries to launch the app
    # store on Windows
    os.execvp("py", ["py", "-3"] + sys.argv)
  except OSError:
    os.execvp("python3", ["python3"] + sys.argv)

import argparse
import pytest
import json
from utils import parse_subtask_score

heading2_map = {
  "Author": "author",
  "Time (ms)": "time",
  "Memory (kb)": "memory",
  "Difficulty": "difficulty",
  "Tags": "tags",
  "Problem Statement": "statement",
  "Constraints": "constraints",
  "Input": "input",
  "Output": "output",
  "Examples": "examples"
}

shallow_headings = {
  'author',
  'time',
  'memory',
  'difficulty',
  'input',
  'output',
  'statement',
}

def main(folder):
  
  # Validate the input file
  test_files_path = os.path.join(os.path.dirname(__file__), 'test_files.py')
  res = pytest.main(['-rs', '--dir', folder, 
    f'{test_files_path}::test_markdown_file_exist',
    f'{test_files_path}::test_markdown_headings_exist',
    f'{test_files_path}::test_markdown_headings_in_order',
    f'{test_files_path}::test_markdown_subtasks',
    f'{test_files_path}::test_markdown_subtasks_sum_one',
    f'{test_files_path}::test_markdown_tags_parsable',
    f'{test_files_path}::test_markdown_example_format'
  ])
  if res:
    return res
  
  # Read and record level 2 records headings
  statement_json = {}
  with open(os.path.join(folder, 'statement.md')) as f:
    current_heading = ''
    for line in f:
      if line.startswith('# '):
        statement_json['name'] = line[2:].strip()
      elif line.startswith('## '):
        if heading2_map[line[2:].strip()] == 'input':
          statement_json['subtasks'] = []
        current_heading = heading2_map[line[2:].strip()]
        statement_json[current_heading] = []
      elif current_heading:
        statement_json[current_heading].append(line)
  
  for key, value in statement_json.items():
    # join lines in shallow headings
    if key in shallow_headings:
      statement_json[key] = ''.join(value).strip()
    if key == 'time' or key == 'memory':
      statement_json[key] = int(statement_json[key])
    # parse tags into a list
    elif key == 'tags':
      line = ''.join(value)
      tags = list(filter(lambda x: bool(x), list(map(lambda x: x.strip(), line.split(',')))))
      statement_json[key] = tags
    # parse the examples into a list
    elif key == 'constraints':
      groups = [['', []]]
      for line in value:
        if line.startswith("### "):
          groups.append([line, []])
        else:
          groups[-1][1].append(line)
      statement_json[key] = ''.join(groups[0][1]).strip()
      subtasks = []
      for group in groups[1:]:
        score = parse_subtask_score(group[0])
        constraints = ''.join(group[1]).strip()
        subtasks.append({'score': score, 'constraints': constraints})
      
      statement_json['subtasks'] = subtasks
    # parse the examples
    elif key == 'examples':
      examples = []
      current_heading = ''
      for line in value:
        if not line.strip():
          continue
        if line.startswith("### ") and line[3:].strip() == "Input":
          examples.append({"input": [], "output": []})
          current_heading = "input"
        elif line.startswith("### ") and line[3:].strip() == "Output":
          current_heading = "output"
        else:
          examples[-1][current_heading].append(line)
      for i in range(len(examples)):
        examples[i]["input"] = ''.join(examples[i]["input"]).strip()[3:-3].strip()
        examples[i]["output"] = ''.join(examples[i]["output"]).strip()[3:-3].strip()
      statement_json[key] = examples
  with open(os.path.join(folder, 'statement.json'), 'w') as f:
    json.dump(statement_json, f, indent=2)


if __name__ == '__main__':

  parser = argparse.ArgumentParser("compile statement.md to statement.json")
  parser.add_argument("folder", help="The folder of the problem")
  args = parser.parse_args()
  exit(main(args.folder))


