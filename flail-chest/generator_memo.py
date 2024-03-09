import json
import random

import json
import random

from itertools import accumulate
from math import gcd, factorial
from collections import deque

def solve(S):
    flag = False
    for i in range(10):
        if S[i: (i + 3)] == 'xxx':
            flag = True
    if flag:
        return "Yes"
    else:
        return "No"


def main():
    test_cases = []
    for _ in range(100):
        IN = ""
        for i in range(12):
            IN += random.choice(['o', 'x'])
        OUT = solve(IN)

        IN += '\n'
        OUT += '\n'

        test_cases.append({
            "input": f"{IN}",
            "output": f"{OUT}"
        })

    print(json.dumps(test_cases, indent = 2))


if __name__ == '__main__':
    main()