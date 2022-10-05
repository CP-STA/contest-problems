## Authored by Kay Akashi ##

def main():
	x, y = map(int, input().split())

	if x > y:
		print('a')
	elif x < y:
		print('b')
	else:
		print('e')

if __name__ == '__main__':
	main()