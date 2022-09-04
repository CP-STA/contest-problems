import subprocess
import json
import numpy as np

gen = np.random.default_rng(99)

test_cases = []

def add_test_case(i, subtask):
  ans = subprocess.run(['./a.out'], input=str(i).encode('utf-8'), capture_output=True).stdout.decode('utf-8').split()
  test_cases.append({
    'input': str(i),
    'output': ans,
    'subtask': subtask
  })  

def add_test_cases(p, subtask):
  for i in p:
    add_test_case(i, subtask)

def add_test_cases_rand(start, end, n, subtask):
  p = gen.choice(np.arange(start, end), n)
  add_test_cases(p, subtask)


for i in range(1, 21):
  add_test_case(i, 1)

p = gen.choice(np.arange(1, 1001), 50)
add_test_cases(p, 2)

p = gen.choice(np.arange(1, 50000), 50)
add_test_cases(p, 3)

p = gen.choice(np.arange(50000, 100001), 50)
add_test_cases(p, 3)

add_test_cases_rand(1, 31, 30, 4)
add_test_cases_rand(31, 10**4 + 1, 30, 4)
add_test_cases_rand(10**4, 10**5, 30, 4)

for i in range(30):
  i = gen.integers(10**14, 10**15)
  add_test_case(i, 4)

add_test_case(10**15, 4)

with open('test-cases.json', 'w') as f:
  json.dump(test_cases, f, indent=2)