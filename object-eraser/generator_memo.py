import json
import random

import json
import random

from itertools import accumulate
from math import gcd, factorial
from collections import deque

def main():
    test_cases = []
    for _ in range(50):
        N = random.randint(1, 10 ** 5)
        K = random.randint(1, 10 ** 12)
        A = []
        for i in range(N):
            a = random.randint(1, 10 ** 9)
            A.append(a)
        IN = str(N) + ' ' + str(K) + '\n'
        A_str = [str(a) for a in A]
        IN += ' '.join(A_str) + '\n'
        A = A[::-1]
        acc = list(accumulate(A))

        cnt = 0
        for i in range(N):
            if acc[i] <= K:
                cnt = i + 1
        OUT = str(cnt) + '\n'

        test_cases.append({
            "input": f"{IN}",
            "output": f"{OUT}"
        })

    print(json.dumps(test_cases, indent = 2))


if __name__ == '__main__':
    main()