import heapq
from operator import mul
from functools import reduce


def solve(K, lists):
    assert K <= reduce(mul, map(len, lists))
    dq = []
    heapq.heappush(dq, (0, (0,) * len(lists)))
    dist = {}
    dist[(0,) * len(lists)] = 0

    for i in range(K-1):
        u, point = heapq.heappop(dq)
        for neighbor in neighbors(point, lists):
            alt = u + distance(point, neighbor, lists)
            if neighbor not in dist or alt < dist[neighbor]:
                dist[neighbor] = alt
                heapq.heappush(dq, (alt, neighbor))
    
    u, ans = heapq.heappop(dq)
    return sum(l[0] for l in lists) - u

def distance(point1, point2, lists):
    assert len(point1) == len(point2) == len(lists)
    return sum(l[i] - l[j] for i, j, l in zip(point1, point2, lists))


def neighbors(point, lists):
    for i, l in enumerate(lists):
        if point[i] + 1 < len(l):
            new_point = list(point)
            new_point[i] += 1
            yield tuple(new_point)

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    print(solve(K, [A, B]))

if __name__ == "__main__":
    main()