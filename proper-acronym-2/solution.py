def main():
	N = int(input())
	li = list(map(str, input().split()))
	S = " "
	for el in li:
		S += el[0]
	T = " " + str(input())

	Ls = len(S)
	Lt = len(T)

	dp = []
	for i in range(Ls):
		cand = [0 for j in range(Lt)]
		dp.append(cand)

	for i in range(1, Ls):
		for j in range(1, Lt):
			if S[i] == T[j]:
				dp[i][j] = max([dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + 1])
			else:
				dp[i][j] = max([dp[i - 1][j], dp[i][j - 1]])

	if dp[Ls - 1][Lt - 1] == Lt - 1:
		print("Yes")
	else:
		print("No")

if __name__ == '__main__':
	main()