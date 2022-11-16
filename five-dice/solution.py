r = int(input())

r -= 5

if r < 0:
    print(0)
    exit(0)

def ways(n, r):
    if r > 5*n:
        return 0
    if n <= 0 and r == 0:
        return 1
    elif n <= 0 and r != 0:
        return 0
    ans = 0
    for i in range(0, min(6, r+1)):
        ans += ways(n-1, r-i)
    return ans

print(ways(5, r))
