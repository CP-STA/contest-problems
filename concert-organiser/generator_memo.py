import json
import random

from itertools import accumulate
from math import gcd
from collections import deque

random.seed(0)

def solve(N, M, connection):
    graph = [[] for _ in range(N)]
    outdeg = [0 for _ in range(N)]

    for el in connection:
        P, Q = el
        P -= 1
        Q -= 1
        graph[Q].append(P)
        outdeg[P] += 1

    sink = deque()
    for i in range(N):
        if outdeg[i] == 0:
            sink.append(i)

    ans = deque()
    while sink:
        pos = sink.popleft()
        ans.appendleft(pos + 1)
        for el in graph[pos]:
            outdeg[el] -= 1
            if outdeg[el] == 0:
                sink.append(el)

    ind = {}
    for i, val in enumerate(ans):
        ind[val] = i

    if len(ans) < N:
        return "No"
    else:
        flag = True
        for P, Q in connection:
            if ind[P] > ind[Q]:
                flag = False
                break
        if flag:
            return "Yes"
        else:
            return "No"

def main():
    test_cases = []
    for _ in range(50):
        N = random.randint(2, 100000)
        M = random.randint(1, 100000)
        connection = []
        for i in range(M):
            P = random.randint(1, N)
            Q = random.randint(2, N)
            if (P == Q):
                Q -= 1
            connection.append([P, Q])
        IN = str(N) + ' ' + str(M) + '\n'
        for el in connection:
            P, Q = el
            IN += str(P) + ' ' + str(Q) + '\n'
        OUT = solve(N, M, connection)

        test_cases.append({
        "input": f"{IN}",
        "output": f"{OUT}"
        })

    print(json.dumps(test_cases, indent = 2))


if __name__ == '__main__':
    main()