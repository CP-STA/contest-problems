import numpy
import json
import random

from itertools import accumulate
from math import gcd
from collections import deque

import heapq

cap = [chr(i) for i in range(65, 65 + 26)]
sml = [chr(i) for i in range(97, 97 + 26)]

def main():
  test_cases = []
  for _ in range(30):
    
    n = random.randint(1, 10)
    name = []
    for i in range(n):
      m = random.randint(1, 10)
      word = random.choice(cap)
      for j in range(m - 1):
        word += random.choice(sml)
      name.append(word)

    acr = ""
    for el in name:
      acr += el[0]

    IN = str(n) + '\n' + ' '.join(name) + '\n' + acr + '\n'
    OUT = "Yes\n"

    test_cases.append({
      "input": f"{IN}",
      "output": f"{OUT}"
    })
  
  print(json.dumps(test_cases, indent=2))


if __name__ == '__main__':
  main()