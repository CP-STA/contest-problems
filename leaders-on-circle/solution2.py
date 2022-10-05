MOD = 10**9 + 7

def moddiv(a, b, m):
    return ((a % m) * (pow(b, -1, m) % m)) % m

def modmul(a, b, m):
    return ((a % m) * (b % m)) % m

Y, X = map(int, input().split())

ans = 1

for i in range(Y-X+1, Y+1):

    ans = modmul(ans, i, MOD)

ans = moddiv(ans, X, MOD)

print(ans)