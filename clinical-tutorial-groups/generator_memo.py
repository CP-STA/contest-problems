import json
import random

import json
import random

from itertools import accumulate
from math import gcd, factorial
from collections import deque

class UnionFind(): # DSU # uf = UnionFind(N) to initialise
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
    def find(self, x): # root of a group x belongs to 
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    def unite(self, x, y): # unite x and y
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    def size(self, x): # size of a group x belong to
        return -self.parents[self.find(x)]
    def same(self, x, y): # judge if x and y are in the same group
        return self.find(x) == self.find(y)
    def members(self, x): # list of members in a group x belongs to
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    def roots(self): # list all roots
        return [i for i, x in enumerate(self.parents) if x < 0]
    def group_count(self): # the number of groups
        return len(self.roots())


def main():
    test_cases = []
    for _ in range(50):
        IN = ''
        OUT = ''

        N = random.randint(2, 100000)
        M1 = random.randint(1, 100000)
        M2 = random.randint(1, 100000)

        IN += str(N) + '\n'

        uf = UnionFind(N)
        li1 = []
        for i in range(M1):
            u = random.randint(1, N)
            v = random.randint(1, N)
            if u != v:
                li1.append([u, v])
        if len(li1) == 0:
            li1.append([1, 2])
        M1 = len(li1)

        li2 = []
        for i in range(M2):
            u = random.randint(1, N)
            v = random.randint(1, N)
            if u != v:
                li2.append([u, v])
        if len(li2) == 0:
            li1.append([1, 2])
        M2 = len(li2)

        IN += str(M1) + '\n'

        for el in li1:
            u = el[0]
            v = el[1]
            IN += str(u) + ' ' + str(v) + '\n'
            u -= 1
            v -= 1
            uf.unite(u, v)
        IN += str(M2) + '\n'
        cnt = 0
        for el in li2:
            u = el[0]
            v = el[1]
            IN += str(u) + ' ' + str(v) + '\n'
            u -= 1
            v -= 1
            if uf.find(u) == uf.find(v):
                cnt += 1

        OUT += str(cnt) + '\n'

        test_cases.append({
            "input": f"{IN}",
            "output": f"{OUT}"
        })

    print(json.dumps(test_cases, indent = 2))


if __name__ == '__main__':
    main()