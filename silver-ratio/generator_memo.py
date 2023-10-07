import numpy
import json
import random
from itertools import accumulate
from math import gcd
from collections import deque
import heapq

random.seed(0);

def solve(q, d):
  return round(d - q / d)

def main():

  test_cases = []

  for _ in range(100):
    q = random.randint(1, 1000)
    d = random.randint(1, 1000)
    INPUT = str(str(q) + " " + str(d))
    OUTPUT = str(solve(q, d))

    test_cases.append({
      "input": f"{INPUT}",
      "output": f"{OUTPUT}"
    })
  
  print(json.dumps(test_cases, indent=2))


if __name__ == '__main__':
  main()