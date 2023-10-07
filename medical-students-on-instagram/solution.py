from collections import deque

def main():
	N, M, C = map(int, input().split())
	P = list(map(int, input().split()))

	for i in range(C):
		P[i] -= 1

	graph = [[] for _ in range(N)]

	for i in range(M):
		x, y = map(int, input().split())
		x -= 1
		y -= 1
		graph[x].append(y)
		graph[y].append(x)

	dist = [float('inf') for _ in range(N)]
	for p in P:
		dist[p] = 0

	data = deque([])
	for p in P:
		data.append(p)
	while data:
		pos = data.popleft()
		for el in graph[pos]:
			if dist[el] == float('inf'):
				dist[el] = dist[pos] + 1
				data.append(el)

	for i in range(N):
		if dist[i] == float('inf'):
			dist[i] = -1

	print(*dist)

if __name__ == '__main__':
	main()