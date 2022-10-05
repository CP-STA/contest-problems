import json
import random

from itertools import accumulate
from math import gcd
from collections import deque


def main():
    test_cases = []
    for _ in range(50):
        X = random.randint(1, 10 ** 6)
        Y = random.randint(1, X)

        IN = str(X) + ' ' + str(Y) + '\n'

        mod = 10 ** 9 + 7

        a = 1
        for i in range(1, X + 1):
            a *= i
            a %= mod
        b = Y
        for i in range(1, X - Y + 1):
            b *= i
            b %= mod
        x = pow(b, mod - 2, mod)
        ans = a * x % mod

        OUT = str(ans) + '\n'

        test_cases.append({
            "input": f"{IN}",
            "output": f"{OUT}"
        })

    print(json.dumps(test_cases, indent = 2))


if __name__ == '__main__':
    main()