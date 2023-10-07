import numpy
import json
import random
from itertools import accumulate
from math import gcd
from collections import deque
import heapq

def num(x, a1, b1, c1, a2, b2, c2):
    return a1 * x * x + b1 * x + c1
def den(x, a1, b1, c1, a2, b2, c2):
    return a2 * x * x + b2 * x + c2

def solve(a1, b1, c1, a2, b2, c2):
  ans = []
  for x in range(-10 ** 5, 10 ** 5):
    if den(x, a1, b1, c1, a2, b2, c2) != 0:
      if num(x, a1, b1, c1, a2, b2, c2) % den(x, a1, b1, c1, a2, b2, c2) == 0 and num(x, a1, b1, c1, a2, b2, c2) // den(x, a1, b1, c1, a2, b2, c2) > 0:
        ans.append(str(x))
  return ans


def main():

  test_cases = []

  for _ in range(100):
    a1 = random.randint(1, 9)
    b1 = random.randint(1, 7)
    c1 = random.randint(1, 7)
    a2 = random.randint(a1 + 1, 10)
    b2 = random.randint(1, 7)
    c2 = random.randint(1, 7)
    INPUT = str(a1) + ' ' + str(b1) + ' ' + str(c1) + ' ' + str(a2) + ' ' + str(b2) + ' ' + str(c2)
    OUTPUT = ''
    if solve(a1, b1, c1, a2, b2, c2) == []:
      OUTPUT = 'None\n'
    else:
      OUTPUT = ' '.join(solve(a1, b1, c1, a2, b2, c2)) + '\n'

    test_cases.append({
      "input": f"{INPUT}",
      "output": f"{OUTPUT}"
    })
  
  print(json.dumps(test_cases, indent=2))


if __name__ == '__main__':
  main()