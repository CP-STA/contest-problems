import json
import random

from itertools import accumulate
from math import gcd
from collections import deque

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
    for _ in range(100):

        routes = set()

        n = random.randint(1, 1000)
        m = random.randint(1, 1000)

        for i in range(m):
            a = random.randint(1, n)
            b = random.randint(1, n)
            if a > b:
                a, b = b, a
            if a != b and (a, b) not in routes:
                routes.add((a, b))

        m = len(routes)
        
        network = []
        for el in routes:
            a, b = el
            network.append([a, b, random.randint(1, 100)])

        s = random.randint(1, n)

        IN = str(n) + ' ' + str(m) + ' ' + str(s) + '\n'

        graph = []
        for i in range(n):
            graph.append([])
        for el in network:
            a, b, c = el

            graph[a - 1].append([b - 1, c])
            graph[b - 1].append([a - 1, c])
            IN += str(a) + ' ' + str(b) + ' ' + str(c) + '\n'

        dist = dijkstra(graph, n, s - 1)

        cnt = 0
        for d in dist:
            if d <= 30:
                cnt += 1

        OUT = str(cnt)

        test_cases.append({
        "input": f"{IN}",
        "output": f"{OUT}"
        })

    print(json.dumps(test_cases, indent = 2))


if __name__ == '__main__':
    main()