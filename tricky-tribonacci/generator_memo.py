import json
import random

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

def solve(p, q, r, x, y, z, k):
    mod = 10 ** 9 + 7

    matrix = [[p, q, r], [1, 0, 0], [0, 1, 0]]
    squares = [matrix]
    for i in range(50):
        matrix = matrix_multiplication_modulo(matrix, matrix, mod)
        squares.append(matrix)

    ans = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    obj = bin(k - 1)[2:][::-1]
    for i in range(len(obj)):
        if obj[i] == '1':
            ans = matrix_multiplication_modulo(ans, squares[i], mod)

    ans = ans[2][0] * z + ans[2][1] * y + ans[2][2] * x
    return ans % mod

import json
import random

from itertools import accumulate
from math import gcd
from collections import deque


def main():
    test_cases = []
    for _ in range(50):
        p = random.randint(1, 10 ** 5)
        q = random.randint(1, 10 ** 5)
        r = random.randint(1, 10 ** 5)
        x = random.randint(1, 10 ** 5)
        y = random.randint(1, 10 ** 5)
        z = random.randint(1, 10 ** 5)
        k = random.randint(1, 10 ** 12)

        IN = str(p) + ' ' + str(q) + ' ' + str(r) + '\n' + str(x) + ' ' + str(y) + ' ' + str(z) + '\n' + str(k)
        OUT = str(solve(p, q, r, x, y, z, k))

        test_cases.append({
            "input": f"{IN}",
            "output": f"{OUT}"
        })

    print(json.dumps(test_cases, indent = 2))


if __name__ == '__main__':
    main()