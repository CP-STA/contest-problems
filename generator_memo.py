import numpy
import json
import random

from itertools import accumulate
from math import gcd
from collections import deque

letters = ['k', 'a', 'y', 'd', 'e', 'o']

def main():
    test_cases = []
    for _ in range(60):

        X = random.randint(1, 10 ** 6)
        Y = random.randint(1, X)

        mod = 10 ** 9 + 7

        IN = str(X) + ' ' + str(Y) + '\n'

        a = 1
        for i in range(1, X + 1):
            a *= i
            a %= mod

        b = 1
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



    print(json.dumps(test_cases, indent=2))


if __name__ == '__main__':
    main()