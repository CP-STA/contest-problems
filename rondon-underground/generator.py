import random 
import json 
from solution import solve
random.seed(123)

problems = []

def no_parallel(n, m, start, end):
    total = 0
    ff = [{i} for i in range(m)]
    lines = []
    while True:
        l = random.randrange(start, end)
        total += l
        if total >= n:
            break
        line = [random.randrange(0,m)]
        for i in range(l-1):
            line.append(random.choice(list({i for i in range(m)} - ff[line[i]])))
            ff[line[i]].add(line[i+1])
            ff[line[i+1]].add(line[i])
        lines.append(line)
    return lines

def with_parallel(n, m, start, end):
    total = 0
    lines = []
    while True:
        l = random.randrange(start, end)
        total += l
        if total > n:
            break
        line = [random.randrange(0,m)]
        for i in range(l-1):
            line.append(random.choice(list({i for i in range(m)} -  set(line))))
        lines.append(line)
    return lines

def choose_station(lines):
    active = set()
    for line in lines:
        active.update(line)
    return random.choice(list(active))

def translate_input(k, m, p, lines):
    o = []
    o.append(f'{k} {m} {p+1} {len(lines)}')
    for line in lines:
        o.append(' '.join(list(map(lambda x: str(x+1), line))))
    return '\n'.join(o)

# Subtask 1
for m in random.choices(list(range(1, 15)), k=10):
    start = random.randrange(m)
    line = [i for i in range(m)]
    k = random.randrange(10**17, 10**18)
    sol = solve(k, len(line), [line], start)
    problems.append(((k, m, start, [line], 1), sol))

problems.append(((2, 2, 0, [[0,1]], 1), (1, 1)))

# Subtask 2 
for _ in range(10):
    n = random.randint(2, 10)
    m = 10
    lines = no_parallel(n, m, 2, min(n, 5))
    p = choose_station(lines)
    k = random.randint(1, 7)
    sol = solve(k, m, lines, p)
    problems.append(((k, m, p, lines, 2), sol))


# Subtask 3
for _ in range(2):
    n = random.randint(2, 10)
    m = 3
    lines = with_parallel(n, m, 2, min(n+1, 4))
    p = choose_station(lines)
    k = random.randint(1, 7)
    sol = solve(k, m, lines, p)
    problems.append(((k, m, p, lines, 3), sol))


for _ in range(3):
    n = random.randint(6, 10)
    m = 3
    lines = with_parallel(n, m, 2, min(n+1, 4))
    p = choose_station(lines)
    k = random.randint(1, 7)
    sol = solve(k, m, lines, p)
    problems.append(((k, m, p, lines, 3), sol))


for _ in range(5):
    n = random.randint(2, 10)
    m = 10
    lines = with_parallel(n, m, 2, min(n+1, 4))
    p = choose_station(lines)
    k = random.randint(1, 7)
    sol = solve(k, m, lines, p)
    problems.append(((k, m, p, lines, 3), sol))

# Subtask 4
for _ in range(10):
    n = random.randint(10, 15)
    m = 15
    lines = no_parallel(n, m, 2, 6)
    p = choose_station(lines)
    k = random.randint(10**17, 10**18)
    sol = solve(k, m, lines, p)
    problems.append(((k, m, p, lines, 4), sol))

# Subtask 5
for _ in range(10):
    n = random.randint(10, 15)
    m = random.randint(5, 10)
    lines = with_parallel(n, m, 2, 6)
    p = choose_station(lines)
    k = random.randint(10**17, 10**18)
    sol = solve(k, m, lines, p)
    problems.append(((k, m, p, lines, 5), sol))

test_cases = []
for problem in problems:
    q, sol = problem
    k, m, p, lines, subtask = q
    test_cases.append({
        'input': translate_input(k, m, p, lines) + '\n',
        'output': ' '.join(list(map(str, sol))) + '\n',
        'subtask': subtask
    })

print(json.dumps(test_cases, indent=4))