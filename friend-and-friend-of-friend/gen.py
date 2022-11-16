import numpy as np
from solution2 import solve
import json
import subprocess
import sys

rng = np.random.default_rng(324)

ps = list(map(lambda p: (np.cos(p*np.pi)/2 + 0.5), rng.random(20)))
ns = list(map(lambda p: int(10**4**p), ps))
ms = list(map(lambda x: min(rng.integers(2, (x**2 - x) // 2, endpoint=True), 10 ** 4), ns))
cases = []

def pair(n, b):
  return (n // b, n % b)

def order(p):
  return(min(*p), max(*p))

def encode(p, b):
  return p[0] * b + p[1]

def is_loop(p):
  return p[0] == p[1]

def canonical(n, b):
  p = pair(n, b)
  p = order(p)
  return encode(p, b)

def shuffle(p):
  flag = rng.integers(0, 2)
  if flag:
    return (min(*p), max(*p))
  else:
    return (max(*p), min(*p)) 

for n, m in zip(ns, ms):
  s = rng.integers(0, n)
  edges = rng.integers(0, n**2, m)
  edges: set = set(map(lambda x: canonical(x, n), edges))
  edges = [x for x in edges if not is_loop(pair(x, n))]
  edges = list(map(lambda x: pair(x, n), edges))
  rng.shuffle(edges)
  edges = list(map(shuffle, edges))
  e = [[] for i in range(n)]
  for p in edges:
    h, u = p
    e[h].append(u)
    e[u].append(h)
  ans = solve(n, e, s)

  input_lines = [f'{n} {s+1} {len(edges)}']
  for edge in edges:
    input_lines.append(f'{edge[0]+1} {edge[1]+1}')
  
  cases.append({
    'input': '\n'.join(input_lines),
    'output': f'{ans}\n'
  })

print(json.dumps(cases, indent=2))