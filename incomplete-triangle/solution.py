## Authored by Kay Akashi ##

def main():
	li = list(map(int, input().split()))
	li.sort()
	r, g, b = li

	ans = max(0, b + 1 - r - g)
	print(ans)

if __name__ == '__main__':
	main()