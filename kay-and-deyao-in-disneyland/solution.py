import heapq

def dijkstra(graph, N, start):
    dist = [float('inf')] * N
    dist[start] = 0
    visited = [False] * N
    visited[start] = True
    heap = [(0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    return dist

N = int(input())

graph = [[] for _ in range(N)]

for i in range(N-1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append((v, w))
    graph[v].append((u, w))

max = 0

for i in range(N):
    dist = dijkstra(graph, N, i)
    for j in range(N):
        if max < dist[j]:
            max = dist[j]

print(max)