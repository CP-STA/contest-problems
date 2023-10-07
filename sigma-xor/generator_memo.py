import numpy
import json
import random
from itertools import accumulate
from math import gcd
from collections import deque
import heapq

def solve(N):
    ans = 0
    if N % 2 == 1:
        g = N // 2 + 1
        if g % 2 == 1:
            ans = 1
    else:
        g = N // 2
        if g % 2 == 1:
            ans = 1
        ans ^= N
    ans ^= 0
    return ans

def main():

  test_cases = []

  for _ in range(49):
    N = random.randint(1, 100000 - 1)
    INPUT = str(N)
    OUTPUT = str(solve(N))

    test_cases.append({
      "input": f"{INPUT}",
      "output": f"{OUTPUT}",
      "subtask": 1
    })

  for _ in range(50):
    N = random.randint(100000, 1000000000000000)
    INPUT = str(N)
    OUTPUT = str(solve(N))

    test_cases.append({
      "input": f"{INPUT}",
      "output": f"{OUTPUT}",
      "subtask": 2
    })
  
  print(json.dumps(test_cases, indent=2))


if __name__ == '__main__':
  main()