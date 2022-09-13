## Authored by Kay Akashi ##

def main():
	n = int(input())
	ans = 0
	i = 1
	while i ** 2 <= n:
		if n % i == 0:
			ans += i
			if i != n // i:
				ans += n // i
		i += 1
	print(ans)

if __name__ == '__main__':
	main()