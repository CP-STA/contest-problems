from math import ceil, floor

def solve(a1, b1, c1, a2, b2, c2):
	p = a2 - a1
	q = b2 - b1
	r = c2 - c1
	if (q ** 2 - 4 * r < 0):
		return []
	else:
		left = int((-q - (q ** 2 - 4 * r) ** 0.5) / (2 * p))
		right = int((-q + (q ** 2 - 4 * r) ** 0.5) / (2 * p))
		ans = []
		for x in range(left - 3, right + 1 + 3):
			if (a2 * x ** 2 + b2 * x + c2 != 0):
				if (a1 * x ** 2 + b1 * x + c1) % (a2 * x ** 2 + b2 * x + c2) == 0 and (a1 * x ** 2 + b1 * x + c1) / (a2 * x ** 2 + b2 * x + c2) > 0:
					ans.append(x)
		return ans

a1, b1, c1, a2, b2, c2 = map(int, input().split())
print(*solve(a1, b1, c1, a2, b2, c2))