import heapq as hq

def main():
    n, m, s = map(int, input().split())
    s -= 1
    e = [[] for i in range(n)] 

    for _ in range(m):
        h, u, w = map(int, input().split())
        h -= 1
        u -= 1
        e[h].append((w, u))
        e[u].append((w, h))
    q = []

    d = [float('inf') for i in range(n)]
    d[s] = 0
    hq.heappush(q, (0, s))

    while q:
        r, h = hq.heappop(q)
        for w, u in e[h]:
            if w + r < d[u]:
                d[u] = w+r
                hq.heappush(q, (w+r, u))
    ans = 0
    for i in range(n):
        if d[i] <= 30:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()