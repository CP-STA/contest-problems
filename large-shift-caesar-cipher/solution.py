n, k = map(int, input().split())

def r(c, k):
    o = ord(c) - ord('a')
    k %= 26 
    o += k
    if o >= 26:
        o -= 26
    return chr(o + ord('a'))

ans = ''.join(list(map(lambda c: r(c, k), list(input()))))
print(ans)