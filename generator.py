import numpy
import json
import random

import heapq
def dijkstra(graph, N, s):
    dist = [float('inf') for _ in range(N)]
    dist[s] = 0

    data = [[0, s]]
    while data:
        pos = heapq.heappop(data)[1]
        for node, cost in graph[pos]:
            if dist[pos] + cost < dist[node]:
                dist[node] = dist[pos] + cost
                heapq.heappush(data, [dist[node], node])
    return dist


def main():
  test_cases = []

  for _ in range(45):
    n = random.randint(1, 1000)
    m = random.randint(1, 1000)
    s = random.randint(1, n)

    IN = str(n) + ' ' + str(m) + ' ' + str(s) + '\n'

    graph = []
    for i in range(n):
      graph.append([])

    sample = set()
    li = []
    for i in range(10 * m):
      a = random.randint(1, n)
      b = random.randint(1, n)
      c = random.randint(1, 100)
      if a > b:
        a, b = b, a
      if (a, b) not in sample:
        li.append([a, b, c])
        sample.add((a, b))

      a -= 1
      b -= 1
      graph[a].append([b, c])
      graph[b].append([a, c])

    if len(li) < m:
      IN = 'INVALID'
    li = li[:m]
    s -= 1
    for el in li:
      a, b, c = el
      IN += str(a) + ' ' + str(b) + ' ' + str(c) + '\n'

    dist = dijkstra(graph, n, s)
    cnt = 0
    for el in dist:
      if el <= 30:
        cnt += 1

    test_cases.append({
      "input": f"{IN}",
      "output": f"{cnt}\n"
    })

  # large_numbers = rng.integers(1, 100000, size = 20)
  # for large_number in large_numbers:
  #   IN = ''
  #   cand = ['k', 'a', 'y', 'd', 'e', 'o']
  #   for i in range(large_number):
  #     IN += random.choice(cand)

  #   test_cases.append({
  #     "input": f"{IN}\n",
  #     "output": f"{result(IN)}\n",
  #     "subtask": 2
  #   })
  
  print(json.dumps(test_cases, indent=2))


if __name__ == '__main__':
  main()