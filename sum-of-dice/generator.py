import random
from solution import solve
import json
import subprocess

def solve(n, k):
    p = subprocess.run('./a.out', input=f"{n} {k}".encode('utf-8'), capture_output=True)
    return list(map(int, p.stdout.split()))

def main():
    random.seed(123)
    test_cases = []
    for _ in range(5):

        n = random.randint(1, 9)
        k = random.randint(1, 45)
        ans = solve(n, k)
        ans = [str(el) for el in ans]
        ans = ' '.join(ans)
        IN = str(n) + ' ' + str(k) + '\n'
        OUT = ans

        test_cases.append({
        "input": f"{IN}",
        "output": f"{OUT}",
        "subtask": 1
        })

    for _ in range(10):

        n = random.randint(1, 10 ** 4 - 5)
        k = random.randint(1, n + 5)
        ans = solve(n, k)
        ans = [str(el) for el in ans]
        ans = ' '.join(ans)
        IN = str(n) + ' ' + str(k) + '\n'
        OUT = ans

        test_cases.append({
        "input": f"{IN}",
        "output": f"{OUT}",
        "subtask": 2
        })
    
    n = 10**4-5
    k = 10**4
    ans = solve(n, k)
    ans = [str(el) for el in ans]
    ans = ' '.join(ans)
    IN = str(n) + ' ' + str(k) + '\n'
    OUT = ans

    test_cases.append({
        "input": f"{IN}",
        "output": f"{OUT}",
        "subtask": 2
    })

    for _ in range(10):

        n = random.randint(1, 10)
        k = random.randint(1, 300)
        ans = solve(n, k)
        ans = [str(el) for el in ans]
        ans = ' '.join(ans)
        IN = str(n) + ' ' + str(k) + '\n'
        OUT = ans

        test_cases.append({
        "input": f"{IN}",
        "output": f"{OUT}",
        "subtask": 3
        })

    for _ in range(2):

        n = int(10**(4+random.random()))
        k = random.randint(1, 300)
        ans = solve(n, k)
        ans = [str(el) for el in ans]
        ans = ' '.join(ans)
        IN = str(n) + ' ' + str(k) + '\n'
        OUT = ans

        test_cases.append({
        "input": f"{IN}",
        "output": f"{OUT}",
        "subtask": 4
        })

    for _ in range(10):

        n = int(10**(4+random.random()))
        k = int(10**(3+random.random()))
        ans = solve(n, k)
        ans = [str(el) for el in ans]
        ans = ' '.join(ans)
        IN = str(n) + ' ' + str(k) + '\n'
        OUT = ans

        test_cases.append({
        "input": f"{IN}",
        "output": f"{OUT}",
        "subtask": 5
        })
    
    n = int(10**5)
    k = int(10**4)
    ans = solve(n, k)
    ans = [str(el) for el in ans]
    ans = ' '.join(ans)
    IN = str(n) + ' ' + str(k) + '\n'
    OUT = ans

    test_cases.append({
    "input": f"{IN}",
    "output": f"{OUT}",
    "subtask": 5
    })

    print(json.dumps(test_cases, indent = 2))

if __name__ == '__main__':
    main()