MOD = 7340033

def polynomial_pow(coefficients, n, modulus, k):
    if n == 0:
        return [1]
    if n % 2 == 0:
        return polynomial_pow(polynomial_mul(coefficients, coefficients, modulus, k), n // 2, modulus, k)[:k]
    else:
        return polynomial_mul(coefficients, polynomial_pow(coefficients, n - 1, modulus, k), modulus, k)[:k]

def polynomial_mul(a, b, modulus, k):
    c = [0 for _ in range(k)]
    for i in range(len(a)):
        for j in range(len(b)):
            if i + j < k:
                c[i + j] = (c[i + j] + a[i] * b[j]) % modulus
    return c

n, k = map(int, input().split())
if k > 300:
    print("none")
else:
    ans = polynomial_pow([1, 1, 1, 1, 1, 1], n, MOD, k)
    print(*ans)