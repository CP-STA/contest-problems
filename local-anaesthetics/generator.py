import json
import random
from math import floor

random.seed(123)

alphabets = [chr(i) for i in range(97, 97 + 26)]
onsets = ['rapid', 'medium', 'slow']
durations = ['long', 'medium', 'short']

def main():
    test_cases = []
    for _ in range(80):

        N = random.randint(1, 1000)
        formulary = []
        names_used = []
        for i in range(N):
            name = ''
            L = random.randint(1, 19)
            for j in range(L):
                name += random.choice(alphabets)
            if name not in names_used:
                formulary.append([name, random.choice(onsets), random.choice(durations)])
        N = len(formulary)

        dic = {}
        for onset in onsets:
            for duration in durations:
                dic[(onset, duration)] = []
        for el in formulary:
            dic[(el[1], el[2])].append(el[0])
        for k in dic:
            dic[k].sort()
            dic[k] = ', '.join(dic[k])

        desired = []
        M = random.randint(1, 1000)

        IN = str(N) + '\n'
        for el in formulary:
            IN += el[0] + ' ' + el[1] + ' ' + el[2] + '\n'
        IN += str(M) + '\n'
        OUT = ''
        for i in range(M):
            onset = random.choice(onsets)
            duration = random.choice(durations)
            IN += onset + ' ' + duration + '\n'
            OUT += (dic[(onset, duration)] if dic[(onset, duration)] else 'NONE') + '\n'

        test_cases.append({
        "input": f"{IN}",
        "output": f"{OUT}"
        })

    print(json.dumps(test_cases, indent = 2))


if __name__ == '__main__':
    main()