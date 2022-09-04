import numpy
import json
import random

from itertools import accumulate
from math import gcd

samples = [[0, 0, 0], [0, 0, 5], [0, 1, 4], [0, 1, 9], [0, 2, 3], [0, 2, 8], [0, 3, 7], [0, 4, 6], [0, 5, 5], [0, 6, 9], [0, 7, 8], [1, 1, 3], [1, 1, 8], [1, 2, 2], [1, 2, 7], [1, 3, 6], [1, 4, 5], [1, 5, 9], [1, 6, 8], [1, 7, 7], [2, 2, 6], [2, 3, 5], [2, 4, 4], [2, 4, 9], [2, 5, 8], [2, 6, 7], [2, 9, 9], [3, 3, 4], [3, 3, 9], [3, 4, 8], [3, 5, 7], [3, 6, 6], [3, 8, 9], [4, 4, 7], [4, 5, 6], [4, 7, 9], [4, 8, 8], [5, 5, 5], [5, 6, 9], [5, 7, 8], [6, 6, 8], [6, 7, 7], [7, 9, 9], [8, 8, 9]]

def blackbox(n, a):
  dic = {}
  for i in range(10):
    dic[i] = 0
  for el in  a:
    dic[el] += 1

  ans = 0
  for sample in samples:
    cand = 1
    appear = {}
    for i in range(10):
      appear[i] = 0
    appear[sample[0]] += 1
    appear[sample[1]] += 1
    appear[sample[2]] += 1

    for i in range(10):
      if appear[i] == 1:
        if dic[i] >= 1:
          cand *= dic[i]
        else:
          cand *= 0
      elif appear[i] == 2:
        if dic[i] >= 2:
          cand *= dic[i] * (dic[i] - 1) // 2
        else:
          cand *= 0
      elif appear[i] == 3:
        if dic[i] >= 3:
          cand *= dic[i] * (dic[i] - 1) * (dic[i] - 2) // 6
        else:
          cand *= 0
    ans += cand

  return ans


def main():
  test_cases = []

  for _ in range(30):

    n = random.randint(3, 100 - 1)
    a = []
    for i in range(n):
      a.append(str(random.randint(0, 100000)))
    IN = str(n) + '\n' + ' '.join(a) + '\n'
    a = [int(el) % 10 for el in a]
    OUT = str(blackbox(n, a)) + '\n'


    test_cases.append({
      "input": f"{IN}",
      "output": f"{OUT}",
      "subtask": 1
    })

  for _ in range(30):

    n = random.randint(100, 100000)
    a = []
    for i in range(n):
      a.append(str(random.randint(0, 100000)))
    IN = str(n) + '\n' + ' '.join(a) + '\n'
    a = [int(el) % 10 for el in a]
    OUT = str(blackbox(n, a)) + '\n'


    test_cases.append({
      "input": f"{IN}",
      "output": f"{OUT}",
      "subtask": 2
    })

  
  print(json.dumps(test_cases, indent=2))


if __name__ == '__main__':
  main()