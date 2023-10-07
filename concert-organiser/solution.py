from collections import deque

def main():
    N, M = map(int, input().split())
    info = []
    graph = [[] for _ in range(N)]
    outdeg = [0 for _ in range(N)]

    for _ in range(M):
        P, Q = map(int, input().split())
        P -= 1
        Q -= 1
        graph[Q].append(P)
        info.append((P, Q))
        outdeg[P] += 1

    sink = deque()
    for i in range(N):
        if outdeg[i] == 0:
            sink.append(i)

    ans = deque()
    while sink:
        pos = sink.popleft()
        ans.appendleft(pos)
        for el in graph[pos]:
            outdeg[el] -= 1
            if outdeg[el] == 0:
                sink.append(el)

    ind = {}
    for i, val in enumerate(ans):
        ind[val] = i

    if len(ans) < N:
        print("No")
    else:
        flag = True
        for P, Q in info:
            if ind[P] > ind[Q]:
                flag = False
                break
        if flag:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()
