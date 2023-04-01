N = int(input())

drugs = dict()

for i in range(N):
    name, a, b = input().split()
    if (a, b) not in drugs:
        drugs[(a, b)] = []
    drugs[(a, b)].append(name)

M = int(input())
for i in range(M):
    a, b = input().split()
    ans = drugs.get((a, b), [])
    ans.sort()
    if ans:
        print(', '.join(ans))
    else:
        print('NONE')
