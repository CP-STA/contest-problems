def a(n, k):
    if k == 0:
        return n == 0
    for i in range(7):
        if a(n-i**i, k-1):
            return True
    return False

n = int(input())
print('Yes' if a(n, 5) else 'No')
