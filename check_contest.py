import argparse
import json
import dateutil.parser
import firebase_admin
from firebase_admin import firestore
from dotenv import load_dotenv
import logging

load_dotenv()

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

firebase_admin.initialize_app()
db = firestore.client()

for problem in info['problems']:
  assert('name' in problem)
  assert('slug' in problem)
  try:
    with open(f"{problem['slug']}/statement.json") as f:
        json.load(f)
  except:
    logging.error(f'Did you remember to compile {problem["slug"]}? You can it with `compile_statement.py -C` or as part of the push process with `push_contest.py`')
    raise
      
  doc_ref = db.collection('problems').document(problem['slug'])
  doc = doc_ref.get()
  if not doc.exists:
    raise ValueError(f"Cannot Find {problem['slug']} in firestore. Did you remember to push it with `push_contest.py`?")

print("All checks passed.")
