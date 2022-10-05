import numpy
import json
import random
import sys

from itertools import accumulate
from math import gcd
from collections import deque

letters = ['k', 'a', 'y', 'd', 'e', 'o']

class LinkedList:
    def __init__(self) -> None:
        self.next_pointers = []
        self.elements = []
        self.L = 0
        self.head = -1 # -1 means tail
    def insert(self, current, ele):
        self.elements.append(ele)
        if current == -1:
            next = self.head
            self.head = self.L
        else:
            next = self.next_pointers[current]
            self.next_pointers[current] = self.L
        self.next_pointers.append(next)
        res = self.L
        self.L += 1
        return res 
    def to_list(self):
        res = []
        next = self.head
        for i in range(self.L):
            res.append(self.elements[next])
            next = self.next_pointers[next]
        return res
    def next(self, current):
        if current == -1:
            return self.head
        else:
            return self.next_pointers[current]

def main():
    test_cases = []
    for _ in range(40):
        random.seed(314)
        li = []
        n = random.randint(1, 10)
        for i in range(n):
            li.append(random.choice(letters))
        s = ''.join(li)
        IN = s

        t = []
        L = 0
        for i in range(n):
            if L <= 2:
                t.append(s[i])
                L += 1
            else:
                t.append(s[i])
                L += 1
                if t[-3] == 'k' and t[-2] == 'a' and t[-1] == 'y':
                    t.pop()
                    t.pop()
                    t.pop()
                    L -= 3
                if L >= 5:
                    if t[-5] == 'd' and t[-4] == 'e' and t[-3] == 'y' and t[-2] == 'a' and t[-1] == 'o':
                        t.pop()
                        t.pop()
                        t.pop()
                        t.pop()
                        t.pop()
                        L -= 5
        OUT = ''.join(t)

        test_cases.append({
            "input": f"{IN}",
            "output": f"{OUT}"
        })

    test_cases.append({
            "input": "kkayadyeyadeyaoo",
            "output": "kadyeyao"
        })
    test_cases.append({
            "input": "deykakayyao",
            "output": ""
        })

    IN = 'k' * 100000
    OUT = 'k' * 100000
    test_cases.append({
            "input": f"{IN}",
            "output": f"{OUT}"
        })

    IN = 'kaydeyao' * 12500
    OUT = ''
    test_cases.append({
            "input": f"{IN}",
            "output": f"{OUT}"
        })
   
    starts = ['ajtrje', 'kdjfte']
    for start in starts:
        bff = LinkedList()
        i = -1
        for c in start:
            i = bff.insert(i, c)
        L = 0
        i = -1
        while L < 4 * 10**5 - 10:
            word = random.choice(['kay', 'deyao'])
            step = random.randint(1, 2)
            for _ in range(step):
                i = bff.next(i)
            j = i
            for c in word:
                j = bff.insert(j, c)
            L += len(word)
        test_cases.append({
            "input": ''.join(bff.to_list()),
            "output": start,
        })
    for test_case in test_cases:
        assert(len(test_case['input']) <=  4 * 10 ** 5)
    print(json.dumps(test_cases, indent=2))

if __name__ == '__main__':
    main()