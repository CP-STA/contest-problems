import numpy
import json
import random

from itertools import accumulate
from math import gcd
from collections import deque

def main():

  test_cases = []

  for _ in range(50):
    n = random.randint(2, 15)
    m = random.randint(2, 15)

    links = []
    links_memo = set()
    for i in range(m):
      a = random.randint(1, n)
      b = random.randint(1, n)
      if a > b:
        a, b = b, a
      if (a, b) not in links_memo and a != b:
        links.append([str(a), str(b)])
        links_memo.add((a, b))
    m = len(links)

    IN = str(n) + ' ' + str(m) + '\n'
    for el in links:
      IN += el[0] + ' ' + el[1] + '\n'

    links = [[int(el[0]) - 1, int(el[1]) - 1] for el in links]

    deg = {}
    for i in range(n):
      deg[i] = 0
    for link in links:
      deg[link[0]] += 1
      deg[link[1]] += 1

    cnt = 0
    for k, v in deg.items():
      if v % 2 == 1:
        cnt += 1

    if cnt == 0 or cnt == 2:
      OUT = 'Yes'
    else:
      OUT = 'No'


    test_cases.append({
      "input": f"{IN}",
      "output": f"{OUT}"
    }) 

  
  print(json.dumps(test_cases, indent=2))


if __name__ == '__main__':
  main()