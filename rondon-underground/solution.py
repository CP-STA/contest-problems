MOD = 10**9 + 7
def make_el(m, lines): # stations numbered from 0 and line is directional
    ff = [[] for _ in range(m)]
    fb = [[] for _ in range(m)]
    als = [[] for _ in range(m)]
    def connect(u, v):
        ff[u].append(v)
        fb[v].append(u)
    for line in lines:
        linea = []
        for i, u in enumerate(line):
            if als[u]:
                up = m
                ff.append([])
                fb.append([])
                m += 1
            else:
                up = u
            linea.append(up)
            als[u].append(up)
            for k in fb[u]:
                connect(k, up)
        for i in range(len(line)-1):
            up=linea[i]
            v=line[i+1]
            for vpp in als[v]:
                connect(up,vpp)
    return m, ff, als

def ajm(m, ff):
    x = [[0 for _ in range(m)] for _ in range(m)]
    for u in range(m):
        for v in ff[u]:
            x[u][v] = 1
    return x

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

def bidir(lines):
    for i in range(len(lines)):
        lines.append(list(reversed(lines[i])))
    return lines

def solve(k, m, lines, u):
    lines = lines.copy()
    n, ff, als = make_el(m,bidir(lines))
    mx = ajm(n, ff)
    mxa=exp(mx,k,n)
    ans1=0
    for upp in als[u]:
       ans1=(mxa[upp][u]+ans1)%MOD
    ans2=0
    for v in range(m):
        for upp in als[u]:   
            ans2=(mxa[upp][v]+ans2)%MOD
    return ans1, ans2

if __name__ == '__main__':
    k, m, p, q = map(int, input().split())
    p -= 1
    lines = []
    for _ in range(q):
       line = list(map(lambda x: int(x) - 1, input().split()))
       lines.append(line)
    print(*solve(k, m, lines, p))

