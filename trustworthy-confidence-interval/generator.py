import numpy
import json
import random
from math import ceil

from itertools import accumulate

random.seed(123)

def solve(N, L, A):
    caterpillar = []
    s = 0
    sq = 0
    for i in range(L):
        s += A[i]
        sq += A[i] ** 2
    caterpillar.append([sq, s])
    for i in range(N - L):
        head = []
        head.append(caterpillar[-1][0] + A[i + L] ** 2 - A[i] ** 2)
        head.append(caterpillar[-1][1] + A[i + L] - A[i])
        caterpillar.append(head)
    CI = []
    for sample in caterpillar:
        lower = ceil(sample[1] / L - 1.96 * ((sample[0] / L - ((sample[1] / L) ** 2)) ** 0.5))
        upper = int(sample[1] / L + 1.96 * ((sample[0] / L - ((sample[1] / L) ** 2)) ** 0.5))
        lower = max(lower, 0)
        upper = min(upper, 1000)
        CI.append([lower, upper])
    ans = [0 for i in range(1030)]
    for ci in CI:
        ans[ci[0]] += 1
        ans[ci[1] + 1] -= 1
    ans = list(accumulate(ans))
    ans = ans[:1001]
    ans = [str(el) for el in ans]
    ans = ' '.join(ans)
    return ans


def main():
    test_cases = []
    for _ in range(50):
        N = random.randint(2, 100)
        L = random.randint(1, N - 1)
        A = [random.randint(200, 800) for i in range(N)]
        OUT = solve(N, L, A)
        A = [str(el) for el in A]
        IN = str(N) + ' ' + str(L) + '\n' + ' '.join(A)
        test_cases.append({
            "input": f"{IN}",
            "output": f"{OUT}",
            "subtask": 1
        })
    for _ in range(50):
        N = random.randint(2, 100000)
        L = random.randint(1, N - 1)
        A = [random.randint(100, 950) for i in range(N)]
        OUT = solve(N, L, A)
        A = [str(el) for el in A]
        IN = str(N) + ' ' + str(L) + '\n' + ' '.join(A)
        test_cases.append({
            "input": f"{IN}",
            "output": f"{OUT}",
            "subtask": 2
        })

    print(json.dumps(test_cases, indent = 2))


if __name__ == '__main__':
    main()