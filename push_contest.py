import json
import os
import push_to_firestore
import firebase_admin
from firebase_admin import firestore
import argparse
import dateutil.parser
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

def main(no_compile=False):
  db = firestore.client()
  with open('upcoming-contest.json') as f:
    contest_id = json.load(f)
  with open(os.path.join("contests", f'{contest_id}.json')) as f:
    contest_info = json.load(f)
  start_time = dateutil.parser.parse(contest_info["info"]['startTime'])
  for problem in contest_info['problems']:
    problem_slug = problem["slug"]
    print(f"pushing {problem_slug}")
    push_to_firestore.main(problem_slug, no_compile=no_compile)
    doc_ref = db.collection('problems').document(problem_slug)
    doc_ref.set({'availableAfter': start_time - timedelta(seconds=2)}, merge=True)
      
      

if __name__ == "__main__":
  parser = argparse.ArgumentParser("Push the contest as defined in upcoming-contest to firebase")
  parser.add_argument('--no-compile', "-N", action="store_true", default=False)
  args = parser.parse_args()
  firebase_admin.initialize_app()
  exit(main(no_compile=args.no_compile))
