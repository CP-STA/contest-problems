import json
import random

from itertools import accumulate
from math import gcd
from collections import deque

random.seed(0)

possible = []
for a in range(8):
    for b in range(8):
        for c in range(8):
            for d in range(8):
                for e in range(8):
                    possible.append(a ** a + b ** b + c ** c + d ** d + e ** e)

possible = list(set(possible))
possible = [el for el in possible if el <= 100000]
for i in range(230):
    possible.append(random.randint(0, 100000))


def main():
    test_cases = []
    for _ in range(100):
        N = random.choice(possible)
        judge = "No"
        for a in range(8):
            for b in range(8):
                for c in range(8):
                    for d in range(8):
                        for e in range(8):
                            if a ** a + b ** b + c ** c + d ** d + e ** e == N:
                                judge = "Yes"
        IN = str(N) + '\n'
        OUT = judge + '\n'

        test_cases.append({
        "input": f"{IN}",
        "output": f"{OUT}"
        })

    print(json.dumps(test_cases, indent = 2))


if __name__ == '__main__':
    main()