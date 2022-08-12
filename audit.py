import argparse
import json
import dateutil.parser


with open('upcoming-contest.json') as f:
  contestSlug = json.load(f)

with open(f'contests/{contestSlug}.json') as f:
  info = json.load(f)
assert('info' in info)
assert('problems' in info)

assert('name' in info['info'])
assert('startTime' in info['info'])
assert('endTime' in info['info'])

dateutil.parser.isoparse(info['info']['startTime'])
dateutil.parser.isoparse(info['info']['endTime'])

for problem in info['problems']:
  assert('name' in problem)
  assert('slug' in problem)
  with open(f'{problem["slug"]}/statement.json') as f:
    statement = json.load(f)
    
