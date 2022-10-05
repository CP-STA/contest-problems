# By Deyao Chen

from multiprocessing.sharedctypes import Value

n = int(input())

ns = []
ns = list(map(int, input().split()))
ns.append(float('inf'))
ns.append(float('-inf'))
ns.sort()

nsb = list(map(lambda x: -x, ns))
nsb.sort()

def bis(a, v, s, e): # includsive, exclusive
    if s + 1 == e:
        return s
    mid = (s + e) // 2
    if a[mid] > v:
        return bis(a, v, s, mid)
    else:
        return bis(a, v, mid, e)

m = int(input())
for i in range(m):
    a, op = input().split()
    a = int(a)
    if op == 'LARGER':
        a = -a 
        arr = nsb
    elif op == 'SMALLER':
        arr = ns
    else:
        raise ValueError()
    p = bis(arr, a, 0, len(arr))
    while arr[p] == a and p > 0:
        p -= 1
    print(p)