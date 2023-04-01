MOD = 10**9 + 7

k, m, p, q = map(int, input().split())
p -= 1
graph = [[] for _ in range(m)]
for i in range(q):
    a = list(map(lambda x: int(x) -1, input().split()))
    for i in range(len(a)-1):
        graph[a[i]].append(a[i+1])
        graph[a[i+1]].append(a[i])

# convert graph to adjacency matrix
adj = [[0 for _ in range(m)] for _ in range(m)]
for i in range(m):
    for j in graph[i]:
        adj[i][j] = 1

def mul(a, b, m):
  c = [[0 for _ in range(m)] for _ in range(m)]
  for i in range(m):
    for j in range(m):
      for k in range(m):
        c[i][j] = (a[i][k] * b[k][j] + c[i][j]) % MOD
  return c

def exp(a, n, m):
  if n == 1:
    return a
  if n % 2 == 0: 
    b = exp(a, n//2, m)
    return mul(b, b, m)
  else:
    return mul(a, exp(a, n-1, m), m)

M = exp(adj, k, m)

sum_of = 0
for i in range(m):
    sum_of += M[p][i]

print(M[p][p], sum_of % MOD)
