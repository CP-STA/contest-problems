## Authored by Kay Akashi ##

from math import gcd

def lcm(x, y):
	return x // gcd(x, y) * y

def main():
	n, a, b = map(int, input().split())
	c = lcm(a, b)
	print(n // c)

if __name__ == '__main__':
	main()