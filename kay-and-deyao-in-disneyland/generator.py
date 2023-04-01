import numpy
import json
import random

from itertools import accumulate
from math import gcd
from collections import deque

import heapq

import numpy as np

random.seed(123)

def generate_random_tree(n, seed = 123):
    rng = np.random.RandomState(seed)
    layer_size = 1
    layer_nodes = [0]
    ff = [[]]
    n -= layer_size
    while n > 0:
        layer_size *= 2
        layer_size = rng.binomial(layer_size * 2, 0.5)
        layer_size = min(n, layer_size)
        new_layer_nodes = [layer_nodes[-1] + 1 + i for i in range(layer_size)]
        ff += [[] for _ in range(layer_size)]
        for node in new_layer_nodes:
            parent = rng.choice(layer_nodes)
            ff[parent].append(node)
        layer_nodes = new_layer_nodes
        n -= layer_size
    p = rng.permutation(len(ff))
    ff = [sorted([p[i] for i in layer]) for layer in ff]
    nff = [[] for _ in range(len(ff))]
    for i, k in enumerate(p):
        nff[k] = ff[i]
    return nff

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

def solve(graph, N):
    dist = dijkstra(graph, N, 0)
    farthest_index = -float('inf')
    farthest_distance = -float('inf')
    for i in range(N):
        if farthest_distance <= dist[i]:
            farthest_index = i
            farthest_distance = dist[i]
    dist_2 = dijkstra(graph, N, farthest_index)
    ans = -float('inf')
    for i in range(N):
        ans = max(ans, dist_2[i])
    return str(ans)

def main():
    test_cases = []
    for _ in range(50):
        N = random.randint(2, 50)
        connection = generate_random_tree(N)
        G = []
        for i in range(N):
            for el in connection[i]:
                G.append([i + 1, el + 1, random.randint(1, 100)])

        graph = [[] for i in range(N)]
        for el in G:
            A, B, C = el
            A -= 1
            B -= 1
            graph[A].append([B, C])
            graph[B].append([A, C])
        OUT = solve(graph, N)
        random.shuffle(G)
        IN = str(N) + '\n'
        G = [[str(el[0]), str(el[1]), str(el[2])] for el in G]
        G = [' '.join(el) for el in G]
        IN += '\n'.join(G)

        test_cases.append({
            "input": f"{IN}",
            "output": f"{OUT}",
            "subtask": 1
        })
    for _ in range(50):
        N = random.randint(2, 5000)
        connection = generate_random_tree(N)
        G = []
        for i in range(N):
            for el in connection[i]:
                G.append([i + 1, el + 1, random.randint(1, 100)])

        graph = [[] for i in range(N)]
        for el in G:
            A, B, C = el
            A -= 1
            B -= 1
            graph[A].append([B, C])
            graph[B].append([A, C])
        OUT = solve(graph, N)
        random.shuffle(G)
        IN = str(N) + '\n'
        G = [[str(el[0]), str(el[1]), str(el[2])] for el in G]
        G = [' '.join(el) for el in G]
        IN += '\n'.join(G)

        test_cases.append({
            "input": f"{IN}",
            "output": f"{OUT}",
            "subtask": 2
        })

    print(json.dumps(test_cases, indent = 2))


if __name__ == '__main__':
    main()