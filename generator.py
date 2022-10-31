import json
import random

from itertools import accumulate
from math import gcd
from collections import deque


def main():
    test_cases = []
    for _ in range(30):
        n = random.randint(1, 10 ** 5)
        dates = []
        for i in range(n):
            year = str(random.randint(1413, 2022)).zfill(4)
            month = str(random.randint(1, 12)).zfill(2)
            date = str(random.randint(1, 28)).zfill(2)
            dates.append(year + '/' + month + '/' + date)
        IN = str(n) + '\n' + '\n'.join(dates)
        dates.sort()
        OUT = dates[0]

        test_cases.append({
        "input": f"{IN}",
        "output": f"{OUT}"
        })

    print(json.dumps(test_cases, indent = 2))


if __name__ == '__main__':
    main()