import json
import random

import json
import random

from itertools import accumulate
from math import gcd, factorial
from collections import deque

def solve(N):
    ans = 0
    for k in range(2, N + 1):
        if k % 2 == 0:
            ans += factorial(N) // factorial(k)
        else:
            ans -= factorial(N) // factorial(k)
    return ans


def main():
    test_cases = []
    for i in range(2, 16):
        IN = str(i) + '\n'
        OUT = str(solve(i)) + '\n'

        test_cases.append({
            "input": f"{IN}",
            "output": f"{OUT}"
        })

    print(json.dumps(test_cases, indent = 2))


if __name__ == '__main__':
    main()