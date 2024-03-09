N, K = map(int, input().split())

words = list(map(int, input().split()))

ans = 0
i = N-1
while K >= words[i] and i >= 0:
    K -= words[i]
    i -= 1
    ans += 1

print(ans)