from math import lcm

n, x = map(int, input().split())
ns = list(map(int, input().split()))

r = lcm(*ns)
if r > x:
    print("-1")
else:
    print(x // r * r)
  