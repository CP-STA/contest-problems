MOD = 1000000007

def matrix_mul(A, B):
    # only for 2x2 matrices
    P = [A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]], [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]
    for i in range(2):
        for j in range(2):
            P[i][j] %= MOD
    return P

def matrix_pow(A, n):
    if n == 1:
        return A
    if n % 2 == 0:
        powered = matrix_pow(A, n/2)
        return matrix_mul(powered, powered)
    else:
        return matrix_mul(A, matrix_pow(A, n-1))

def solution(p, q, n):
    if n == 0:
        return 1
    M = [[p, q], [0, 1]]
    Mp = matrix_pow(M, n)
    return (Mp[0][0] + Mp[0][1]) % MOD

def main():
    p, q = map(int, input().split())
    n = int(input())
    print(solution(p, q, n-1))

if __name__ == "__main__":
    main()