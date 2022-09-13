## Authored by Kay Akashi ##

import heapq

def main():
	q = int(input())

	queue = []
	heapq.heapify(queue)

	dic = {}

	for _ in range(q):
		li = list(map(str, input().split()))
		if li[0] == 'IN':
			dic[int(li[2])] = li[1]
			heapq.heappush(queue, int(li[2]))
		else:
			least = heapq.heappop(queue)
			second_least = heapq.heappop(queue)
			print(dic[second_least])
			heapq.heappush(queue, least)
			heapq.heappush(queue, second_least)

if __name__ == '__main__':
	main()