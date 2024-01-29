def num(x, a1, b1, c1, a2, b2, c2):
    return a1 * x * x + b1 * x + c1
def den(x, a1, b1, c1, a2, b2, c2):
    return a2 * x * x + b2 * x + c2

def solve(a1, b1, c1, a2, b2, c2):
  ans = []
  for x in range(-10 ** 5, 10 ** 5):
        if (a2*x**2+b2*x+c2) != 0 and (a1*x**2+b1*x+c1)//(a2*x**2+b2*x+c2) > 0 and (a1*x**2+b1*x+c1) % (a2*x**2+b2*x+c2) == 0:
            ans.append(str(x))
  return ans

a1, b1, c1, a2, b2, c2 = map(int, input().split())
ans = solve(a1, b1, c1, a2, b2, c2)
if ans:
  print(*ans)
else:
  print('None')
