from itertools import product
n = int(input())
a = list(map(int, input().split()))
a.sort()

for i in range(1, n+1):
    for p in product(a, repeat=i):
        p = map(str, p)
        print(''.join(p), end=' ')
