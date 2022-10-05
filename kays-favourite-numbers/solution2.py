n = int(input())
a = set(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
for i in b:
    if i in a:
        ans += 1

print(ans + 1)
