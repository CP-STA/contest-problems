import json
import random

import json
import random

from itertools import accumulate
from math import gcd, factorial
from collections import deque

def annoying(A, B, Lx, Ly):
    Ax = A[0]
    Ay = A[1]
    Bx = B[0]
    By = B[1]

    flag1 = False
    S11 = Lx * Ay - Ly * Ax
    S12 = Lx * By - Ly * Bx
    if (S11 * S12 < 0):
        flag1 = True
    
    flag2 = False
    S21 = (Bx - Ax) * (-Ay) - (By - Ay) * (-Ax)
    S22 = (Bx - Ax) * (Ly - Ay) - (By - Ay) * (Lx - Ax)
    if (S21 * S22 < 0):
        flag2 = True

    flag3 = False
    if (Lx * Ay == Ly * Ax and abs(Ax) < abs(Lx)):
        flag3 = True
    if (Lx * By == Ly * Bx and abs(Bx) < abs(Lx)):
        flag3 = True
    if (Ax * By == Ay * Bx and (Ax * Bx < 0 or Ay * By < 0)):
        flag3 = True
    if ((Ly - Ay) * (Bx - Lx) == (Lx - Ax) * (By - Ly) and ((Lx - Ax) * (Lx - Bx) < 0 or (Ly - Ay) * (Ly - By) < 0)):
        flag3 = True

    return (flag1 and flag2) or (flag3)
    

def main():
    test_cases = []
    for _ in range(120):
        N = random.randint(1, 500)
        Kx = random.randint(0, 200)
        Ky = random.randint(0, 200)
        Lx = random.randint(0, 200)
        Ly = random.randint(0, 200)
        if Kx == Lx and Ky == Ly:
            continue
        li = []
        for i in range(N):
            X = random.randint(0, 200)
            Y = random.randint(0, 200)
            if ([X, Y] not in li) and ([X, Y] != [Kx, Ky]) and ([X, Y] != [Lx, Ly]):
                li.append([X, Y])
        N = len(li)
        IN = str(N) + '\n' + str(Kx) + ' ' + str(Ky) + ' ' + str(Lx) + ' ' + str(Ly) + '\n'
        for el in li:
            IN += str(el[0]) + ' ' + str(el[1]) + '\n'
        Lx -= Kx
        Ly -= Ky
        for i in range(N):
            li[i][0] -= Kx
            li[i][1] -= Ky

        cnt = 0
        for i in range(N - 1):
            for j in range(i + 1, N):
                if annoying(li[i], li[j], Lx, Ly):
                    cnt += 1

        OUT = str(cnt) + '\n'

        test_cases.append({
            "input": f"{IN}",
            "output": f"{OUT}"
        })

    print(json.dumps(test_cases, indent = 2))


if __name__ == '__main__':
    main()