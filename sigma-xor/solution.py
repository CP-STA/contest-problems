# Authored by Kay Akashi #

def solve():
	N = int(input())
	ans = 0
	if N % 2 == 1:
		g = N // 2 + 1
		if g % 2 == 1:
			ans = 1
	else:
		g = N // 2
		if g % 2 == 1:
			ans = 1
		ans ^= N
	ans ^= 0
	print(ans)

solve()