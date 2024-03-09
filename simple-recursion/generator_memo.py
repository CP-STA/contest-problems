import json
import random

from heapq import heapify, heappop, heappush

from itertools import accumulate
from math import gcd, factorial
from collections import deque

def matrix_multiplication_modulo(A, B, mod):
    a = len(A)
    b = len(A[0])
    c = len(B[0])
    M = []
    for i in range(a):
        M.append([])
    for i in range(a):
        for k in range(c):
            M[i].append(0)
    for i in range(a):
        for k in range(c):
            s = 0
            for j in range(b):
                s += A[i][j] * B[j][k]
                s %= mod
            M[i][k] = s
    return M

def solve(p, q, X):
    mod = 10 ** 9 + 7
    s = bin(X - 1)[2:]
    s = s[::-1]
    li = [[[p, q], [0, 1]]]
    for i in range(50):
        M = li[-1]
        li.append(matrix_multiplication_modulo(M, M, mod))
    ans = [[1], [1]]
    for i in range(len(s)):
        if s[i] == '1':
            ans = matrix_multiplication_modulo(li[i], ans, mod)
    return ans[0][0]



def main():
    test_cases = []
    for _ in range(50):
        p = random.randint(1, 3000)
        q = random.randint(1, 3000)
        X = random.randint(1, 10000)
        IN = str(p) + ' ' + str(q) + '\n' + str(X) + '\n'
        OUT = str(solve(p, q, X)) + '\n'
        test_cases.append({
            "input": f"{IN}",
            "output": f"{OUT}",
            "subtask": 1
        })

    for _ in range(50):
        p = random.randint(1, 3000)
        q = random.randint(1, 3000)
        X = random.randint(1, 1000000000000)
        IN = str(p) + ' ' + str(q) + '\n' + str(X) + '\n'
        OUT = str(solve(p, q, X)) + '\n'
        test_cases.append({
            "input": f"{IN}",
            "output": f"{OUT}",
            "subtask": 2
        })
    print(json.dumps(test_cases, indent = 2))


if __name__ == '__main__':
    main()