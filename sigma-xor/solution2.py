from math import log
a = int(input())+1

length = int(log(a, 2))+1
ans = [0] * length
for i in range(1, length):
    rem = a % (2**i * 2)
    rem = max(rem - 2**i, 0)
    ans[i] = rem % 2
rem = a % 4
if rem in [0, 1]:
    ans[0] = 0
elif rem in [2, 3]:
    ans[0] = 1
else:
    raise RuntimeError('condition not exhaustive')

ans_d = 0
for i in range(length):
    ans_d += ans[i] * 2**i
print(ans_d)
