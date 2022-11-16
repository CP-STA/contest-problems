n, k = map(int, input().split())

s = list(map(int, input().split()))

if 2*k >= max(s) - min(s):
    print("Yes")
else:
    print("No")