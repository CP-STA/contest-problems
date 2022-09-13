import numpy
import json
import random

from itertools import accumulate
from math import gcd

def blackbox(n):
  i = 1
  ans = 0
  while i ** 2 <= n:
    if n % i == 0:
      ans += i
      if n // i != i:
        ans += n // i
    i += 1
  return ans

def main():

  test_cases = []

  IN = '1' + '\n'
  OUT = str(blackbox(1)) + '\n'
  test_cases.append({
    "input": f"{IN}",
    "output": f"{OUT}",
    "subtask": 1
  })

  for _ in range(30):

    n = random.randint(1, 100 - 1)
    IN = str(n) + '\n'
    OUT = str(blackbox(n)) + '\n'

    test_cases.append({
      "input": f"{IN}",
      "output": f"{OUT}",
      "subtask": 1
    })

  IN = '99' + '\n'
  OUT = str(blackbox(99)) + '\n'
  test_cases.append({
    "input": f"{IN}",
    "output": f"{OUT}",
    "subtask": 1
  })

  for _ in range(30):

    n = random.randint(100, 100000 - 1)
    IN = str(n) + '\n'
    OUT = str(blackbox(n)) + '\n'

    test_cases.append({
      "input": f"{IN}",
      "output": f"{OUT}",
      "subtask": 2
    })

  IN = '99999' + '\n'
  OUT = str(blackbox(99999)) + '\n'
  test_cases.append({
    "input": f"{IN}",
    "output": f"{OUT}",
    "subtask": 2
  })


  for _ in range(30):

    n = random.randint(100000, 10000000000)
    IN = str(n) + '\n'
    OUT = str(blackbox(n)) + '\n'

    test_cases.append({
      "input": f"{IN}",
      "output": f"{OUT}",
      "subtask": 3
    })

  IN = '10000000000' + '\n'
  OUT = str(blackbox(10000000000)) + '\n'
  test_cases.append({
    "input": f"{IN}",
    "output": f"{OUT}",
    "subtask": 3
  })
  
  print(json.dumps(test_cases, indent=2))


if __name__ == '__main__':
  main()