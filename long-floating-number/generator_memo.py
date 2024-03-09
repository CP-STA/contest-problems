import json
import random

import json
import random

from itertools import accumulate
from math import gcd, factorial
from collections import deque

def main():
    test_cases = []
    for _ in range(70):
        first = random.randint(0, 1)

        IN = str(first) + '.'
        OUT = ""
        zero = random.randint(0, 1)
        length = random.randint(1, 990)
        if zero:
            IN += '0' * length + '\n'
            if first == 0:
                OUT = "smaller\n"
            else:
                OUT = "equal\n"
        else:
            for i in range(length):
                IN += str(random.randint(0, 9))
            IN += '\n'
            if first == 0:
                OUT = "smaller\n"
            else:
                OUT = "larger\n"

        test_cases.append({
            "input": f"{IN}",
            "output": f"{OUT}"
        })

    print(json.dumps(test_cases, indent = 2))


if __name__ == '__main__':
    main()