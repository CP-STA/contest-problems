## Authored by Kay Akashi ##

def main():
	n = int(input())

	li = list(map(str, input().split()))
	li = [el[0] for el in li]
	acr = ''.join(li)


	s = str(input())

	if s == acr:
		print('Yes')
	else:
		print('No')

if __name__ == '__main__':
	main()