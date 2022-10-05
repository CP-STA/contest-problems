def main():
	X, Y = map(int, input().split())
	mod = 10 ** 9 + 7

	a = 1
	for i in range(1, X + 1):
		a *= i
		a %= mod

	b = Y
	for i in range(1, X - Y + 1):
		b *= i
		b %= mod

	x = pow(b, mod - 2, mod)

	ans = a * x % mod
	print(ans)

if __name__ == '__main__':
	main()