from math import ceil, floor

N, L = map(int, input().split())
A = list(map(int, input().split()))
C = [(sum(A[:L])/L, sum(map(lambda x: x**2, A[:L]))/L)]
for i in range(N-L):
    C.append((C[-1][0] + (A[i+L] - A[i])/L, C[-1][1] + (A[i+L]**2 - A[i]**2)/L))

changes = [0] * 1002
for i in range(N-L+1):
    lower_ci = C[i][0] - 1.96 * (C[i][1] - C[i][0]**2)**0.5
    upper_ci = C[i][0] + 1.96 * (C[i][1] - C[i][0]**2)**0.5
    changes[max(0, ceil(lower_ci))] += 1
    changes[min(1001, floor(upper_ci)+1)] -= 1

results = []
k = 0
for i in range(1001):
    k += changes[i]
    results.append(k)

print(' '.join(map(str, results)))