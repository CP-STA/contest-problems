n = int(input())

m = dict()
def moves(n):
  if n in m:
    return m[n]
  else:
    if n >= 1:
      ans = moves(n - 3) + moves(n - 1)
    else:
      ans = 1
    m[n] = ans
    return ans

print(moves(n) % (10**9 + 7))
