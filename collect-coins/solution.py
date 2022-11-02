t = int(input())

c = list(map(int, input().split()))

ans = 0

for j in c:
    ans += j
    if ans < 0:
        ans = 0
    elif ans > 10:
        ans = 10

print(ans)