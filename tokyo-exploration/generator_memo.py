import json
import random

from heapq import heapify, heappop, heappush

from itertools import accumulate
from math import gcd, factorial
from collections import deque

def solve(N, M, K, A, B):
    A.sort()
    B.sort()
    seen = set()
    seen.add((N - 1, M - 1))
    S = [[-(A[N - 1] + B[M - 1]), N - 1, M - 1]]
    heapify(S)
    price = []
    L = 0
    while (L < K):
        MM = heappop(S)
        price.append(-MM[0])
        L += 1
        I = MM[1]
        J = MM[2]
        if I > 0:
            if (I - 1, J) not in seen:
                heappush(S, [-(A[I - 1] + B[J]), I - 1, J])
                seen.add((I - 1, J))
        if J > 0:
            if (I, J - 1) not in seen:
                heappush(S, [-(A[I] + B[J - 1]), I, J - 1])
                seen.add((I, J - 1))
    return price[K - 1]


def main():
    test_cases = []
    for _ in range(50):
        N = random.randint(1, 100)
        M = random.randint(1, 100)
        K = random.randint(1, N + M)
        A = [random.randint(1, 10 ** 9) for i in range(N)]
        B = [random.randint(1, 10 ** 9) for i in range(M)]
        OUT = str(solve(N, M, K, A, B))
        IN = str(N) + ' ' + str(M) + ' ' + str(K) + '\n'
        A = [str(a) for a in A]
        B = [str(b) for b in B]
        IN += ' '.join(A) + '\n'
        IN += ' '.join(B) + '\n'
        test_cases.append({
            "input": f"{IN}",
            "output": f"{OUT}",
            "subtask": 1
        })

    for _ in range(50):
        N = random.randint(1, 100000)
        M = random.randint(1, 100000)
        K = random.randint(1, N + M)
        A = [random.randint(1, 10 ** 9) for i in range(N)]
        B = [random.randint(1, 10 ** 9) for i in range(M)]
        OUT = str(solve(N, M, K, A, B))
        IN = str(N) + ' ' + str(M) + ' ' + str(K) + '\n'
        A = [str(a) for a in A]
        B = [str(b) for b in B]
        IN += ' '.join(A) + '\n'
        IN += ' '.join(B) + '\n'
        test_cases.append({
            "input": f"{IN}",
            "output": f"{OUT}",
            "subtask": 2
        })
    print(json.dumps(test_cases, indent = 2))


if __name__ == '__main__':
    main()