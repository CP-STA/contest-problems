q, d = map(int, input().split())
p = d-q/d
pp = p

a0 = 1
a1 = 1
for i in range(1000):
    a2 = p*a1 + q*a0
    a0 = a1
    a1 = a2
    a1 /= a0
    a0 = 1
if round(a1/a0) != d:
    raise ValueError()

print(round(pp))
