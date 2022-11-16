from collections import deque

def main():
	n, x, m = map(int, input().split())
	x -= 1

	graph = [[] for i in range(n)]
	for i in range(m):
		a, b = map(int, input().split())
		a -= 1
		b -= 1
		graph[a].append(b)
		graph[b].append(a)

	seen = [False for i in range(n)]
	dist = [float('inf') for i in range(n)]
	seen[x] = True
	dist[x] = 0

	data = [x]
	data = deque(data)
	while data:
		pos = data.popleft()
		for el in graph[pos]:
			if seen[el]:
				continue
			else:
				seen[el] = True
				data.append(el)
				if dist[el] == float('inf'):
					dist[el] = dist[pos] + 1

	cnt = 0
	for d in dist:
		if 0 <= d <= 2:
			cnt += 1

	if len(graph[x]) == 0:
		cnt = 0
	print(cnt)

if __name__ == '__main__':
	main()