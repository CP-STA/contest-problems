MOD = 10**9 + 7

def div(a, b, m):
    return a // b

def mul(a, b, m):
    return a * b

Y, X = map(int, input().split())

ans = 1

for i in range(Y-X+1, Y+1):

    ans = mul(ans, i, MOD)

ans = div(ans, X, MOD)

print(ans % MOD)