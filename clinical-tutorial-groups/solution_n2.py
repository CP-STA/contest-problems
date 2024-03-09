N = int(input())
M1 = int(input())
reps = [-1] * N
for _ in range(M1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if reps[a] == -1 and reps[b] == -1:
        reps[a] = a
        reps[b] = a
    elif reps[a] != -1 and reps[b] != -1:
        correct = reps[a]
        incorrect = reps[b]
        for i in range(N):
            if reps[i] == incorrect:
                reps[i] = correct
    elif reps[a] == -1 and reps[b] != -1:
        reps[a] = reps[b]
    elif reps[b] == -1 and reps[a] != -1:
        reps[b] = reps[a]
    else:
        raise ValueError('If statement is not exhaustive')
M2 = int(input())
ans = 0
for _ in range(M2):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if reps[a] == reps[b] and reps[a] != -1:
        ans += 1

print(ans)
