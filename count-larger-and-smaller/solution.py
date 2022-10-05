def main():
	n = int(input())
	a = list(map(int, input().split()))
	a.sort()

	largest = {}
	smallest = {}
	for el in a:
		largest[el] = -1
		smallest[el] = n
	for i in range(n):
		largest[a[i]] = i
	for i in range(n - 1, -1, -1):
		smallest[a[i]] = i

	m = int(input())
	for _ in range(m):
		x, op = map(str, input().split())
		x = int(x)
		if op == 'LARGER':
			flag = True
			left = -1
			right = n
			while left + 1 < right:
				mid = (left + right) // 2
				if a[mid] < x:
					left = mid
				elif x < a[mid]:
					right = mid
				else:
					print((n - 1) - (largest[a[mid]] + 1) + 1)
					flag = False
					break
			if flag:
				if x < a[0]:
					print(n)
				elif a[n - 1] <= x:
					print(0)
				else:
					print(n - right)
		else:
			flag = True
			left = -1
			right = n
			while left + 1 < right:
				mid = (left + right) // 2
				if a[mid] < x:
					left = mid
				elif x < a[mid]:
					right = mid
				else:
					print(smallest[a[mid]])
					flag = False
					break
			if flag:
				if a[n - 1] < x:
					print(n)
				elif x <= a[0]:
					print(0)
				else:
					print(right)

if __name__ == '__main__':
	main()