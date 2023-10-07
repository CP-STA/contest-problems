def solve(q, d):
	return round(d - q / d)

q, d = map(int, input().split())
print(solve(q, d))