## Authored by Kay Akashi ##

def main():
	n = int(input())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))

	s = set()
	for el in a:
		s.add(el)

	cnt = 0
	for el in b:
		if el in s:
			cnt += 1
	print(cnt)

if __name__ == '__main__':
	main()