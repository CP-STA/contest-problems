import numpy as np
import json

rng = np.random.default_rng(3337)

ns = rng.integers(1, 500, 20)

def sol(n):
  return n**2 * 21

cases = [{'input': '0\n', 'output': '0\n'}]

for n in ns:
  cases.append({
    'input': f'{n}\n',
    'output': f'{sol(n)}\n'
  })

print(json.dumps(cases, indent=2))
