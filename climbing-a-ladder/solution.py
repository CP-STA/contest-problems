#!/usr/bin/env python3

MOD = 10**9 + 7
M = [
  [1, 0, 1],
  [1, 0, 0],
  [0, 1, 0]
]
def mul(a, b):
  c = [[0, 0, 0] for _ in range(3)]
  for i in range(3):
    for j in range(3):
      for k in range(3):
        c[i][j] = (a[i][k] * b[k][j] + c[i][j]) % MOD
  return c

def exp(a, n):
  if n == 1:
    return a
  if n % 2 == 0: 
    b = exp(a, n//2)
    return mul(b, b)
  else:
    return mul(a, exp(a, n-1))

n = int(input())

if n == 1:
  print(2)
elif n == 2:
  print(3)
elif n == 3:
  print(4)
else:
  S = exp(M, n-3)
  fn0 = (S[0][0] * 2 + S[0][1] + S[0][2]) % MOD
  fn1 = (S[1][0] * 2 + S[1][1] + S[1][2]) % MOD
  fn2 = (S[2][0] * 2 + S[2][1] + S[2][2]) % MOD
  print((fn0 + fn1 + fn2) % MOD)