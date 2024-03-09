import json
import random

import json
import random

from itertools import accumulate
from math import gcd, factorial
from collections import deque

def main():
    test_cases = []
    cnt = 0
    for _ in range(500):
        IN = ""
        L = []
        R = []
        for i in range(4):
            l = random.randint(0, 9)
            r = random.randint(l + 1, 10)
            L.append(l)
            R.append(r)
            IN += str(l) + ' ' + str(r) + '\n'
        M = max(L)
        m = min(R)
        ans = max(0, m - M)
        OUT = str(max(0, m - M)) + '\n'

        if ans <= 2:
            cnt += 1

        if (cnt <= 50):
            test_cases.append({
                "input": f"{IN}",
                "output": f"{OUT}"
            })
        else:
            if (ans >= 3):
                test_cases.append({
                    "input": f"{IN}",
                    "output": f"{OUT}"
                })         

    print(json.dumps(test_cases, indent = 2))


if __name__ == '__main__':
    main()