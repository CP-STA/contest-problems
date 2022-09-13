import numpy
import json
import random

from itertools import accumulate
from math import gcd

letters = [chr(i) for i in range(97, 97 + 26)]

def blackbox(s, t):
  dic = {}
  for i in range(len(s)):
    dic[s[i]] = 0
  for i in range(len(s)):
    dic[s[i]] += 1
  for i in range(len(t)):
    dic[t[i]] -= 1

  li = []
  for k, v in dic.items():
    li.append([k, v])
  li.sort()
  li = [el for el in li if el[1] != 0]
  li = [el[0] + ' ' + str(el[1]) for el in li]
  return li


def main():

  test_cases = []

  for _ in range(40):

    s = []
    n = random.randint(1, 1000000)
    m = random.randint(1, n)
    for i in range(n):
      s.append(random.choice(letters))
    t = random.sample(s, k = m)

    s = ''.join(s)
    t = ''.join(t)

    IN = s + '\n' + t + '\n'
    OUT = ''
    for el in blackbox(s, t):
      OUT += el + '\n'

    if OUT == '':
      OUT += '\n'

    test_cases.append({
      "input": f"{IN}",
      "output": f"{OUT}"
    })

  n = 1000000
  m = 911444
  s = []
  for i in range(n):
    s.append(random.choice(letters))
  t = random.sample(s, k = m)

  s = ''.join(s)
  t = ''.join(t)

  IN = IN = s + '\n' + t + '\n'
  OUT = ''
  for el in blackbox(s, t):
    OUT += el + '\n'

  if OUT == '':
    OUT += '\n'

  test_cases.append({
    "input": f"{IN}",
    "output": f"{OUT}"
  })

  IN = 'edgecase\nedgecase\n'
  OUT = '\n'
  test_cases.append({
    "input": f"{IN}",
    "output": f"{OUT}"
  })



  # for _ in range(30):

  #   n = random.randint(100, 100000)
  #   a = []
  #   for i in range(n):
  #     a.append(str(random.randint(0, 100000)))
  #   IN = str(n) + '\n' + ' '.join(a) + '\n'
  #   a = [int(el) % 10 for el in a]
  #   OUT = str(blackbox(n, a)) + '\n'


  #   test_cases.append({
  #     "input": f"{IN}",
  #     "output": f"{OUT}",
  #     "subtask": 2
  #   })

  
  print(json.dumps(test_cases, indent=2))


if __name__ == '__main__':
  main()