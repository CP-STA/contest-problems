def ccw(A,B,C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

def is_between(a, b, c):
    crossproduct = (c[1] - a[1]) * (b[0] - a[0]) - (c[0] - a[0]) * (b[1] - a[1])

    # compare versus epsilon for floating point values, or != 0 if using integers
    if abs(crossproduct) != 0:
        return False

    dotproduct = (c[0] - a[0]) * (b[0] - a[0]) + (c[1] - a[1])*(b[1] - a[1])
    if dotproduct < 0:
        return False

    squaredlengthba = (b[0] - a[0])*(b[0] - a[0]) + (b[1] - a[1])*(b[1] - a[1])
    if dotproduct > squaredlengthba:
        return False

    return True
# Return true if line segments AB and CD intersect
def intersect(A,B,C,D):
    return \
        (ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)) or \
        is_between(A, B, C) or \
        is_between(A, B, D) or \
        is_between(C, D, A) or \
        is_between(C, D, B)


N = int(input())
Kx, Ky, Lx, Ly = map(int, input().split())
K = (Kx, Ky)
L = (Lx, Ly)

points = []

for _ in range(N):
    a, b = map(int, input().split())
    points.append((a, b))
ans = 0
for i in range(N):
    for j in range(i+1, N):
        if intersect(K, L, points[i], points[j]):
            # print(i, j)
            ans += 1

print(ans)