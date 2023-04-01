_, T = map(int, input().split())
W = list(map(int, input().split()))

dpm = [[-1 for i in range(101)] for i in range(10**4+1)]

def dp(r, c):
    if c == 0:
        return (0 if r == 0 else float('inf'))
    if dpm[r][c] != -1:
        return dpm[r][c]
    elif W[c-1] > r:
        dpm[r][c] = dp(r, c-1)
        return dpm[r][c]
    else:
        dpm[r][c] = min(1+dp(r-W[c-1], c-1), dp(r, c-1))
        return dpm[r][c]
   

ans = dp(T, len(W))
if ans == float('inf'):
    ans = -1

print(ans)