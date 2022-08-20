import re

def parse_subtask_score(line):
  results = re.search(r'\((.*)\)', line[3:])
  return float(results.group(1))
