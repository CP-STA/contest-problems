## Authored by Kay Akashi ##

def main():
	X, Y, Z = map(int, input().split())
	fare = X + (Z // 1000) * Y
	print(fare)

if __name__ == '__main__':
	main()