def is_cycle(i, n, graph, visited, path):
    visited[i] = True
    path[i] = True
    for nei in graph[i]:
        if visited[nei] == False:
            if is_cycle(nei, n, graph, visited, path):
                return True
        elif path[nei]:
            return True
    path[i] = False
    return False

def has_cycle(n, graph):
    visited = [False for i in range(n)]
    path = [False for i in range(n)]
    for i in range(n):
        if not visited[i] and is_cycle(i, n, graph, visited, path):
            return True
    return False

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    graph[a].append(b)

print('No' if has_cycle(N, graph) else 'Yes')
