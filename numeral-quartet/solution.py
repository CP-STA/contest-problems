ans = []

def dfs(s, A, B, C, D, K):
	if len(s) < K:
		s1 = s + str(A)
		s2 = s + str(B)
		s3 = s + str(C)
		s4 = s + str(D)
		ans.append(s1)
		ans.append(s2)
		ans.append(s3)
		ans.append(s4)
		dfs(s1, A, B, C, D, K)
		dfs(s2, A, B, C, D, K)
		dfs(s3, A, B, C, D, K)
		dfs(s4, A, B, C, D, K)

K = int(input())
A, B, C, D = map(int, input().split())

dfs('', A, B, C, D, K)
ans = [int(el) for el in ans]
ans.sort()
print(*ans)