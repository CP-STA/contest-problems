import json
import random

from itertools import accumulate
from math import gcd
from collections import deque

random.seed(0);

def solve(N, M, C, P, graph):

    dist = [float('inf') for _ in range(N)]
    for p in P:
        dist[p] = 0

    data = deque([])
    for p in P:
        data.append(p)
    while data:
        pos = data.popleft()
        for el in graph[pos]:
            if dist[el] == float('inf'):
                dist[el] = dist[pos] + 1
                data.append(el)

    for i in range(N):
        if dist[i] == float('inf'):
            dist[i] = -1
    dist = [str(el) for el in dist]
    return dist

def main():
    test_cases = []
    for _ in range(20):
        N = random.randint(2, 100)
        M = random.randint(1, 350)
        C = random.randint(1, N)

        students = [i for i in range(1, N + 1)]
        P = random.sample(students, C)

        IN = str(N) + ' ' + str(M) + ' ' + str(C) + '\n'
        for p in P:
            IN += str(p) + ' '
        IN = IN[:-1] + '\n'

        graph = [[] for i in range(N)]

        used = set()
        L = 0
        while True:
            if L == M:
                break
            x = random.randint(1, N - 1)
            y = random.randint(x + 1, N)
            if (x, y) not in used:
                L += 1
                used.add((x, y))
                graph[x - 1].append(y - 1)
                graph[y - 1].append(x - 1)
                IN += str(x) + ' ' + str(y) + '\n'

        for i in range(C):
            P[i] = P[i] - 1

        OUT = ''
        for el in solve(N, M, C, P, graph):
            OUT += el + ' '
        OUT = OUT[:-1]
        OUT += '\n'


        test_cases.append({
            "input": f"{IN}",
            "output": f"{OUT}",
            "subtask": 1
        })

    for _ in range(10):
        N = random.randint(2, 400000)
        M = random.randint(1, 500000)
        C = random.randint(1, N)

        students = [i for i in range(1, N + 1)]
        P = random.sample(students, C)

        IN = str(N) + ' ' + str(M) + ' ' + str(C) + '\n'
        for p in P:
            IN += str(p) + ' '
        IN = IN[:-1] + '\n'

        graph = [[] for i in range(N)]

        used = set()
        L = 0
        while True:
            if L == M:
                break
            x = random.randint(1, N - 1)
            y = random.randint(x + 1, N)
            if (x, y) not in used:
                L += 1
                used.add((x, y))
                graph[x - 1].append(y - 1)
                graph[y - 1].append(x - 1)
                IN += str(x) + ' ' + str(y) + '\n'

        for i in range(C):
            P[i] = P[i] - 1

        OUT = ''
        for el in solve(N, M, C, P, graph):
            OUT += el + ' '
        OUT = OUT[:-1]
        OUT += '\n'


        test_cases.append({
            "input": f"{IN}",
            "output": f"{OUT}",
            "subtask": 2
        })

    print(json.dumps(test_cases, indent=2))


if __name__ == '__main__':
    main()
