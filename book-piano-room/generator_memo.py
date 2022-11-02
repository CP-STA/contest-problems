import json
import random

from itertools import accumulate
from math import gcd
from collections import deque

def solve(n, li):
    book = [0 for _ in range(n)]
    for el in li:
        l = el[0]
        r = el[1]
        l -= 1
        r -= 1

        book[l] += 1
        if r != n - 1:
            book[r + 1] -= 1

    book = list(accumulate(book))

    cnt = sum(book[i] == 0 for i in range(n))
    return cnt

def main():
    test_cases = []
    for _ in range(30):
        n = random.randint(1, 99)
        m = random.randint(1, 99)

        li = []
        for i in range(m):
            l = random.randint(1, n)
            r = random.randint(l, n)
            li.append([l, r])

        ans = solve(n, li)

        li = [[str(el[0]), str(el[1])] for el in li]
        li = [' '.join(el) for el in li]

        IN = str(n) + ' ' + str(m) + '\n' + '\n'.join(li)
        OUT = str(ans)

        test_cases.append({
        "input": f"{IN}",
        "output": f"{OUT}",
        "subtask": 1
        })

    for _ in range(30):
        n = random.randint(100, 10 ** 5)
        m = random.randint(100, 10 ** 5)

        li = []
        for i in range(m):
            l = random.randint(1, n)
            r = random.randint(l, n)
            li.append([l, r])

        ans = solve(n, li)

        li = [[str(el[0]), str(el[1])] for el in li]
        li = [' '.join(el) for el in li]

        IN = str(n) + ' ' + str(m) + '\n' + '\n'.join(li)
        OUT = str(ans)

        test_cases.append({
        "input": f"{IN}",
        "output": f"{OUT}",
        "subtask": 2
        })

    print(json.dumps(test_cases, indent = 2))


if __name__ == '__main__':
    main()