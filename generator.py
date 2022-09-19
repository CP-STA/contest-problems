import numpy
import json
import random

from itertools import accumulate
from math import gcd
from collections import deque

def bb(g, y, r, t):
    t %= (g + 2 * y + r)
    if 0 <= t < g:
        return "green"
    elif g <= t < g + y:
        return "yellow"
    elif g + y <= t < g + y + r:
        return "red"
    else:
        return "yellow"


def main():
    test_cases = []
    for _ in range(80):
        g = random.randint(1, 100)
        y = random.randint(1, 100)
        r = random.randint(1, 100)
        t = random.randint(0, 86400)
        IN = str(g) + ' ' + str(y) + ' ' + str(r) + '\n' + str(t) + '\n'
        OUT = bb(g, y, r, t) + '\n'
        test_cases.append({
            "input": f"{IN}",
            "output": f"{OUT}"
        })

    print(json.dumps(test_cases, indent=2))


if __name__ == '__main__':
    main()