import argparse
import compile_statement
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import firestore
import os
import json

load_dotenv()

def main(problem_id, no_compile=False):
  if not no_compile:
    res = compile_statement.main(problem_id)
    if res:
      return res

  db = firestore.client()
  with open(os.path.join(problem_id, "statement.json")) as f:
    data = json.load(f)
    doc_ref = db.collection('problems').document(problem_id)
    doc_ref.set(data)


if __name__ == '__main__':
  parser = argparse.ArgumentParser("Push a contest problem to firebase")
  parser.add_argument("problem_id", help="The problem id. Usually it's just the name of the folder")
  parser.add_argument('--no-compile', "-N", action="store_true", default=False)
  args = parser.parse_args()
  firebase_admin.initialize_app()
  exit(main(args.problem_id, no_compile=args.no_compile))

