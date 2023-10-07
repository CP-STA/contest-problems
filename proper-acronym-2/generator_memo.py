import json
import random

from itertools import accumulate
from math import gcd
from collections import deque

random.seed(0);

def solve(N, S, T):
    S = " " + S
    T = " " + T

    Ls = len(S)
    Lt = len(T)

    dp = []
    for i in range(Ls):
        cand = [0 for j in range(Lt)]
        dp.append(cand)

    for i in range(1, Ls):
        for j in range(1, Lt):
            if S[i] == T[j]:
                dp[i][j] = max([dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + 1])
            else:
                dp[i][j] = max([dp[i - 1][j], dp[i][j - 1]])

    return dp[Ls - 1][Lt - 1] == Lt - 1

head = [chr(i) for i in range(65, 65 + 26)]
for i in range(10):
    head.append(str(i))
tail = [chr(i) for i in range(97, 97 + 26)]
for i in range(10):
    head.append(str(i))

def main():
    test_cases = []
    for _ in range(50):
        N = random.randint(1, 10)
        S = ""
        for i in range(N):
            S += random.choice(head)
        IN = str(N) + '\n'
        for i in range(N):
            word = S[i]
            for j in range(random.randint(1, 7)):
                word += random.choice(tail)
            IN += word + ' '
        IN = IN[:-1]
        IN += '\n'
        valid = random.randint(0, 1)
        T = ""
        if valid == 1:
            ind = random.sample(range(0, N), k = random.randint(1, N))
            ind.sort()
            for i in range(len(ind)):
                T += S[ind[i]]
            IN += T + '\n'
            OUT = "Yes" + '\n'
        else:
            ind = random.sample(range(0, N), k = random.randint(1, N))
            for i in range(len(ind)):
                T += S[ind[i]]
            IN += T + '\n'
            if solve(N, S, T):
                OUT = "Yes" + '\n'
            else:
                OUT = "No" + '\n'


        test_cases.append({
            "input": f"{IN}",
            "output": f"{OUT}",
            "subtask": 1
        })

    for _ in range(50):
        N = random.randint(1, 5000)
        S = ""
        for i in range(N):
            S += random.choice(head)
        IN = str(N) + '\n'
        for i in range(N):
            word = S[i]
            for j in range(random.randint(1, 7)):
                word += random.choice(tail)
            IN += word + ' '
        IN = IN[:-1]
        IN += '\n'
        valid = random.randint(0, 1)
        T = ""
        if valid == 1:
            ind = random.sample(range(0, N), k = random.randint(1, N))
            ind.sort()
            for i in range(len(ind)):
                T += S[ind[i]]
            IN += T + '\n'
            OUT = "Yes" + '\n'
        else:
            ind = random.sample(range(0, N), k = random.randint(1, N))
            for i in range(len(ind)):
                T += S[ind[i]]
            IN += T + '\n'
            if solve(N, S, T):
                OUT = "Yes" + '\n'
            else:
                OUT = "No" + '\n'

        test_cases.append({
            "input": f"{IN}",
            "output": f"{OUT}",
            "subtask": 2
        })

    print(json.dumps(test_cases, indent=2))


if __name__ == '__main__':
    main()