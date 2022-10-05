import json
import random

from itertools import accumulate
from math import gcd
from collections import deque

def solve(n, a, m, li):
    a.sort()

    largest = {}
    smallest = {}
    for el in a:
        largest[el] = -1
        smallest[el] = n
    for i in range(n):
        largest[a[i]] = i
    for i in range(n - 1, -1, -1):
        smallest[a[i]] = i

    OUT = ''
    for el in li:
        x, op = el
        if op == 'LARGER':
            flag = True
            left = -1
            right = n
            while left + 1 < right:
                mid = (left + right) // 2
                if a[mid] < x:
                    left = mid
                elif x < a[mid]:
                    right = mid
                else:
                    OUT += str((n - 1) - (largest[a[mid]] + 1) + 1) + '\n'
                    flag = False
                    break
            if flag:
                if x < a[0]:
                    OUT += str(n) + '\n'
                elif a[n - 1] <= x:
                    OUT += str(0) + '\n'
                else:
                    OUT += str(n - right) + '\n'
        else:
            flag = True
            left = -1
            right = n
            while left + 1 < right:
                mid = (left + right) // 2
                if a[mid] < x:
                    left = mid
                elif x < a[mid]:
                    right = mid
                else:
                    OUT += str(smallest[a[mid]]) + '\n'
                    flag = False
                    break
            if flag:
                if a[n - 1] < x:
                    OUT += str(n) + '\n'
                elif x <= a[0]:
                    OUT += str(0) + '\n'
                else:
                    OUT += str(right) + '\n'
    return OUT

def main():
    test_cases = []
    for _ in range(30):
        n = random.randint(1, 99)
        m = random.randint(1, 99)
        a = []
        for i in range(n):
            a.append(random.randint(-300, 300))
        li = []
        for i in range(m):
            x = random.randint(-300, 300)
            op = ''
            if random.randint(0, 1) == 0:
                op = 'SMALLER'
            else:
                op = 'LARGER'
            el = [x, op]
            li.append(el)

        OUTPUT = solve(n, a, m, li)
        a = [str(el) for el in a]
        random.shuffle(a)
        li = [[str(el[0]), el[1]] for el in li]
        INPUT = str(n) + '\n' + ' '.join(a) + '\n' + str(m) + '\n'
        for el in li:
            INPUT += el[0] + ' ' + el[1] + '\n'
        test_cases.append({
            "input": f"{INPUT}",
            "output": f"{OUTPUT}",
            "subtask": 1
        })

    INPUT = '4\n10 11 12 13\n4\n2 SMALLER\n2 SMALLER\n2 SMALLER\n2 SMALLER\n'
    OUTPUT = '0\n0\n0\n0\n'
    test_cases.append({
        "input": f"{INPUT}",
        "output": f"{OUTPUT}",
        "subtask": 1
    })

    for _ in range(30):
        n = random.randint(100, 100000)
        m = random.randint(100, 100000)
        a = []
        for i in range(n):
            a.append(random.randint(-100000, 100000))
        li = []
        for i in range(m):
            x = random.randint(-100000, 100000)
            op = ''
            if random.randint(0, 1) == 0:
                op = 'SMALLER'
            else:
                op = 'LARGER'
            el = [x, op]
            li.append(el)

        OUTPUT = solve(n, a, m, li)
        a = [str(el) for el in a]
        random.shuffle(a)
        li = [[str(el[0]), el[1]] for el in li]
        INPUT = str(n) + '\n' + ' '.join(a) + '\n' + str(m) + '\n'
        for el in li:
            INPUT += el[0] + ' ' + el[1] + '\n'
        test_cases.append({
            "input": f"{INPUT}",
            "output": f"{OUTPUT}",
            "subtask": 2
        })

    for _ in range(1):
        n = 100000
        m = 100000
        a = []
        for i in range(n):
            a.append(random.randint(-100000, 100000))
        li = []
        for i in range(m):
            x = random.randint(-100000, 100000)
            op = ''
            if random.randint(0, 1) == 0:
                op = 'SMALLER'
            else:
                op = 'LARGER'
            el = [x, op]
            li.append(el)

        OUTPUT = solve(n, a, m, li)
        a = [str(el) for el in a]
        random.shuffle(a)
        li = [[str(el[0]), el[1]] for el in li]
        INPUT = str(n) + '\n' + ' '.join(a) + '\n' + str(m) + '\n'
        for el in li:
            INPUT += el[0] + ' ' + el[1] + '\n'
        test_cases.append({
            "input": f"{INPUT}",
            "output": f"{OUTPUT}",
            "subtask": 2
        })

    for _ in range(1):
        n = 100000
        m = 100000
        a = []
        for i in range(n):
            a.append(random.randint(-100000, 100000))
        li = []
        x = random.randint(-100000, 100000)
        op = 'LARGER'
        for i in range(m):
            el = [x, op]
            li.append(el)

        OUTPUT = solve(n, a, m, li)
        a = [str(el) for el in a]
        random.shuffle(a)
        li = [[str(el[0]), el[1]] for el in li]
        INPUT = str(n) + '\n' + ' '.join(a) + '\n' + str(m) + '\n'
        for el in li:
            INPUT += el[0] + ' ' + el[1] + '\n'
        test_cases.append({
            "input": f"{INPUT}",
            "output": f"{OUTPUT}",
            "subtask": 2
        })

    print(json.dumps(test_cases, indent=2))


if __name__ == '__main__':
    main()