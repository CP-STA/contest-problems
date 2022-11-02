from itertools import accumulate

def solve(n, li):
	book = [0 for _ in range(n)]
	for el in li:
		l = el[0]
		r = el[1]
		l -= 1
		r -= 1

		book[l] += 1
		if r != n - 1:
			book[r + 1] -= 1

	book = list(accumulate(book))

	cnt = sum(book[i] == 0 for i in range(n))
	print(cnt)

solve()