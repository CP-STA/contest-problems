import numpy
import json
import random

from itertools import accumulate
from math import gcd
from collections import deque

import heapq

def main():
  test_cases = []
  for _ in range(50):
    r = random.randint(1, 30)
    g = random.randint(1, 30)
    b = random.randint(1, 30)

    IN = str(r) + ' ' + str(g) + ' ' + str(b) + '\n'

    li = [r, g, b]
    li.sort()
    r, g, b = li
    OUT = str(max(0, b + 1 - r - g))
    test_cases.append({
      "input": f"{IN}",
      "output": f"{OUT}"
    })
  
  print(json.dumps(test_cases, indent=2))


if __name__ == '__main__':
  main()