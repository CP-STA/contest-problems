import numpy
import json
import random

from itertools import accumulate
from math import gcd
from collections import deque

def main():

  test_cases = []

  for _ in range(50):
    n = random.randint(2, 10 ** 4)
    x = random.randint(1, n)
    m = random.randint(2, 10 ** 4)

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

    IN = str(n) + ' ' + str(x) + ' ' + str(m) + '\n'
    for el in links:
      IN += el[0] + ' ' + el[1] + '\n'

    links = [[int(el[0]) - 1, int(el[1]) - 1] for el in links]
    x -= 1


    graph = [[] for i in range(n)]
    for link in links:
      graph[link[0]].append(link[1])
      graph[link[1]].append(link[0])

    seen = [False for i in range(n)]
    dist = [float('inf') for i in range(n)]
    seen[x] = True
    dist[x] = 0

    data = [x]
    data = deque(data)
    while data:
      pos = data.popleft()
      for el in graph[pos]:
        if seen[el]:
          continue
        else:
          seen[el] = True
          data.append(el)
          if dist[el] == float('inf'):
            dist[el] = dist[pos] + 1
    cnt = 0
    for d in dist:
      if 0 <= d <= 2:
        cnt += 1

    if len(graph[x]) == 0:
      cnt = 0

    OUT = str(cnt) + '\n'

    test_cases.append({
      "input": f"{IN}",
      "output": f"{OUT}"
    })

  test_cases.append({
    "input": "7 2 4\n1 5\n5 3\n3 4\n7 6\n",
    "output": "0"
  })  

  
  print(json.dumps(test_cases, indent=2))


if __name__ == '__main__':
  main()