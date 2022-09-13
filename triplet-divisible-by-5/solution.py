def main():
	n = int(input())
	a = list(map(int, input().split()))

	a = [el % 5 for el in a]

	dic = {}
	for el in a:
		dic[el] = 0
	for el in a:
		dic[el] += 1

	samples = [[0, 0, 0], [0, 1, 4], [0, 2, 3], [1, 1, 3], [1, 2, 2], [2, 4, 4], [3, 3, 4]]

	ans = 0
	for sample in samples:
		appear = {}
		for i in range(3):
			appear[sample[i]] = 0
		for i in range(3):
			appear[sample[i]] += 1

		cand = 1
		for k, v in appear.items():
			if k not in dic:
				cand *= 0
			else:
				if dic[k] < v:
					cand *= 0
				else:
					if v == 1:
						cand *= dic[k]
					elif v == 2:
						cand *= dic[k] * (dic[k] - 1) // 2
					elif v == 3:
						cand *= dic[k] * (dic[k] - 1) * (dic[k] - 2) // 6
		ans += cand

	print(ans)

if __name__ == '__main__':
	main()