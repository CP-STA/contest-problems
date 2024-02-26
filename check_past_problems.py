import json
import os

def main():
  with open('past-problems.json') as f:
    problems = json.load(f)

  for problem in problems:
    assert('name' in problem)
    assert('slug' in problem)
    assert('date' in problem)
    assert('difficulty' in problem)
    with open(f'{os.path.join(problem["slug"], "statement.json")}') as f:
      statement = json.load(f)
      assert statement["difficulty"] == problem["difficulty"], f"difficulties in index and in problem are not the same for {problem['slug']}"
  print("past-problems.json checks passed.")
  return 0


if __name__ == '__main__':
  exit(main())
