import numpy
import json
import random

from itertools import accumulate
from math import gcd
from collections import deque

import heapq

vegetable = []
for i in range(100000):
  l = random.randint(1, 10)
  name = []
  for j in range(l):
    name.append(chr(random.randint(97, 97 + 25)))
  name = ''.join(name)
  vegetable.append(name)

vegetable = list(set(vegetable))
L = len(vegetable)
quantity = random.sample(range(0, 100000), k = L)

dic = {}
for i in range(L):
  dic[quantity[i]] = vegetable[i]

def main():

  test_cases = []

  for _ in range(30):

    q = random.randint(3, 99)

    commands = []
    ins = random.randint(3, q)
    outs = q - ins

    quantities = random.sample(quantity, k = ins)
    for i in range(ins):
      commands.append(['IN', dic[quantities[i]], str(quantities[i])])

    for i in range(outs):
      commands.append(['OUT'])

    pre = commands[:3]
    post = commands[3:]
    random.shuffle(post)

    commands = pre + post

    INPUT = str(q) + '\n'
    for command in commands:
      INPUT += ' '.join(command) + '\n'

    for command in commands:
      if len(command) == 3:
        command[2] = int(command[2])

    OUTPUT = ''

    queue = []
    heapq.heapify(queue)
    for command in commands:
      if command[0] == 'IN':
        heapq.heappush(queue, command[2])
      else:
        least = heapq.heappop(queue)
        second_least = heapq.heappop(queue)
        OUTPUT += dic[second_least] + '\n'
        heapq.heappush(queue, second_least)
        heapq.heappush(queue, least)


    test_cases.append({
      "input": f"{INPUT}",
      "output": f"{OUTPUT}",
      "subtask": 1
    })

  for _ in range(30):

    q = random.randint(100, 10 ** 4)

    commands = []
    ins = random.randint(3, q)
    outs = q - ins

    quantities = random.sample(quantity, k = ins)
    for i in range(ins):
      commands.append(['IN', dic[quantities[i]], str(quantities[i])])

    for i in range(outs):
      commands.append(['OUT'])

    pre = commands[:3]
    post = commands[3:]
    random.shuffle(post)

    commands = pre + post

    INPUT = str(q) + '\n'
    for command in commands:
      INPUT += ' '.join(command) + '\n'

    for command in commands:
      if len(command) == 3:
        command[2] = int(command[2])

    OUTPUT = ''

    queue = []
    heapq.heapify(queue)
    for command in commands:
      if command[0] == 'IN':
        heapq.heappush(queue, command[2])
      else:
        least = heapq.heappop(queue)
        second_least = heapq.heappop(queue)
        OUTPUT += dic[second_least] + '\n'
        heapq.heappush(queue, second_least)
        heapq.heappush(queue, least)


    test_cases.append({
      "input": f"{INPUT}",
      "output": f"{OUTPUT}",
      "subtask": 2
    })
  
  print(json.dumps(test_cases, indent=2))


if __name__ == '__main__':
  main()