import json
import random

from itertools import accumulate
from math import gcd
from collections import deque

random.seed(0);

ans = []

def dfs(s, A, B, C, D, K):
    global ans
    if len(s) < K:
        s1 = s + str(A)
        s2 = s + str(B)
        s3 = s + str(C)
        s4 = s + str(D)
        ans.append(int(s1))
        ans.append(int(s2))
        ans.append(int(s3))
        ans.append(int(s4))
        dfs(s1, A, B, C, D, K)
        dfs(s2, A, B, C, D, K)
        dfs(s3, A, B, C, D, K)
        dfs(s4, A, B, C, D, K)


def main():
    global ans
    test_cases = []
    for _ in range(30):
        ans = []
        K = random.randint(1, 5)
        A = random.randint(1, 6)
        B = random.randint(A + 1, 7)
        C = random.randint(B + 1, 8)
        D = random.randint(C + 1, 9)
        dfs('', A, B, C, D, K)
        IN = str(K) + '\n' + str(A) + ' ' + str(B) + ' ' + str(C) + ' ' + str(D) + '\n'
        OUT = ''
        ans.sort()
        for el in ans:
            OUT += str(el) + ' '
        OUT = OUT[:-1]

        test_cases.append({
            "input": f"{IN}",
            "output": f"{OUT}",
            "subtask": 1
        })

    for _ in range(30):
        ans = []
        K = random.randint(5, 9)
        A = random.randint(1, 6)
        B = random.randint(A + 1, 7)
        C = random.randint(B + 1, 8)
        D = random.randint(C + 1, 9)
        dfs('', A, B, C, D, K)
        IN = str(K) + '\n' + str(A) + ' ' + str(B) + ' ' + str(C) + ' ' + str(D) + '\n'
        OUT = ''
        ans.sort()
        for el in ans:
            OUT += str(el) + ' '
        OUT = OUT[:-1]

        test_cases.append({
            "input": f"{IN}",
            "output": f"{OUT}",
            "subtask": 2
        })

    print(json.dumps(test_cases, indent=2))


if __name__ == '__main__':
    main()