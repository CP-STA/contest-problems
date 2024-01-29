N, M, C = map(int, input().split())
graph = [[] for i in range(N)]
distance = [-1 for i in range(N)]
queue = list(map(lambda x: int(x) - 1, input().split()))
for _ in range(M):
    x, y = map(lambda x: int(x) - 1, input().split())
    graph[x].append(y)
    graph[y].append(x)

d = 0
while queue:
    seen = set()
    new_queue = []
    for i in queue:
        if i not in seen and distance[i] == -1:
            distance[i] = d
            seen.add(i)
            for nei in graph[i]:
                new_queue.append(nei)
    queue = new_queue
    d += 1

print(*distance)
