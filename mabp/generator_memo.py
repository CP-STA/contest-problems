import json
import random

from itertools import accumulate
from math import gcd
from collections import deque

random.seed(4)

def main():
    test_cases = []
    for _ in range(100):
        D = random.randint(65, 140)
        M = random.randint(D, 140)

        S = 3 * M - 2 * D
        
        IN = str(M) + ' ' + str(D) + '\n'
        OUT = str(3 * M - 2 * D) + '\n'

        if (S <= 140):
            test_cases.append({
            "input": f"{IN}",
            "output": f"{OUT}"
            })

    print(json.dumps(test_cases, indent = 2))


if __name__ == '__main__':
    main()