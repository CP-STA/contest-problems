import numpy
import json
import random

from itertools import accumulate
from math import gcd
from collections import deque

small_numbers = [i for i in range(1, 201)]
numbers = [i for i in range(1, 10 ** 7 + 1)]

def main():

  test_cases = []

  for _ in range(30):

    n = random.randint(1, 99)
    a = random.sample(small_numbers, k = n)
    b = []
    for i in range(n):
      b.append(random.choice(small_numbers))

    random.shuffle(a)
    random.shuffle(b)

    s = set(a)
    cnt = 0
    for el in b:
      if el in s:
        cnt += 1
    a = [str(el) for el in a]
    b = [str(el) for el in b]
    IN = str(n) + '\n' + ' '.join(a) + '\n' + ' '.join(b) + '\n'
    OUT = str(cnt)


    test_cases.append({
      "input": f"{IN}",
      "output": f"{OUT}",
      "subtask": 1
    })

  for _ in range(30):

    n = random.randint(100, 10 ** 5)
    a = random.sample(numbers, k = n)
    b = []
    for i in range(n):
      b.append(random.choice(numbers))

    random.shuffle(a)
    random.shuffle(b)

    s = set(a)
    cnt = 0
    for el in b:
      if el in s:
        cnt += 1

    a = [str(el) for el in a]
    b = [str(el) for el in b]

    IN = str(n) + '\n' + ' '.join(a) + '\n' + ' '.join(b) + '\n'
    OUT = str(cnt)


    test_cases.append({
      "input": f"{IN}",
      "output": f"{OUT}",
      "subtask": 2
    })

  
  print(json.dumps(test_cases, indent=2))


if __name__ == '__main__':
  main()