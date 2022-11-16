import heapq
def dijkstra(graph, N, s):
    dist = [float('inf') for _ in range(N)]
    dist[s] = 0

    data = [[0, s]]
    while data:
        pos = heapq.heappop(data)[1]
        for node, cost in graph[pos]:
            if dist[pos] + cost < dist[node]:
                dist[node] = dist[pos] + cost
                heapq.heappush(data, [dist[node], node])
    return dist


def main():
    n, m, s = map(int, input().split())
    graph = []
    for i in range(n):
        graph.append([])

    for i in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append([b, c])
        graph[b].append([a, c])

    dist = dijkstra(graph, n, s - 1)

    cnt = 0
    for el in dist:
        if el <= 30:
            cnt += 1


    print(cnt)

if __name__ == '__main__':
    main()