import numpy
import json
import random

from math import ceil, log2

def ispow2(n):
    return (n & (n - 1) == 0) and n != 0

def ceilpow2(n):
    return 2 ** ceil(log2(n))

def extend0(a: list, n):
    for i in range(n - len(a)):
        a.append(0)

MOD = 7340033
ROOT = 5
ROOT_1 = 4404020
ROOT_PW = 2**20

def make_nfft(MOD, ROOT, ROOT_1, ROOT_PW):
    def add(a, b):
        return (a + b) % MOD

    def mul(a, b):
        return (a * b) % MOD

    def mod_inverse(n):
        return pow(n, -1, MOD)

    def div(a, b):
        return mul(a, mod_inverse(b))

    def nfft(a, invert):
        n = len(a)
        if not ispow2(n):
            raise ValueError("Length of a has to be a power of 2")
        if n == 1:
            return a.copy()
        a0 = [a[2 * i] for i in range(n // 2)]
        a1 = [a[2 * i + 1] for i in range(n // 2)]
        y0 = nfft(a0, invert)
        y1 = nfft(a1, invert)
        y = [0 for i in range(n)]
        if invert:
            wlen = pow(ROOT_1, ROOT_PW // n, MOD)
        else:
            wlen = pow(ROOT, ROOT_PW // n, MOD)
        w = 1
        for i in range(n // 2):
            y[i] = add(y0[i], mul(w, y1[i]))
            y[i + n // 2] = add(y0[i], -mul(w, y1[i]))
            i_2 = mod_inverse(2)
            if invert:
                y[i] = mul(y[i], i_2)
                y[i + n // 2] = mul(y[i + n // 2], i_2)
            w = mul(w, wlen)
        return y

    def mul_polynomial(a, b):
        n = ceilpow2(len(a) + len(b))
        a = a.copy()
        b = b.copy()
        extend0(a, n)
        extend0(b, n)
        af = nfft(a, False)
        bf = nfft(b, False)
        pf = [0 for i in range(n)]
        for i in range(n):
            pf[i] = mul(af[i], bf[i])
        p = nfft(pf, True)
        return p

    def pow_polynomial(a, n, k):
        if n == 1:
            return a[:k]
        a = a[:k]
        if not n & 1:
            b = pow_polynomial(a, n // 2, k)
            return mul_polynomial(b, b)[:k]
        else:
            return mul_polynomial(pow_polynomial(a, n - 1, k), a)[:k]

    return nfft, mul_polynomial, pow_polynomial

nfft, mul_polynomial, pow_polynomial = make_nfft(MOD, ROOT, ROOT_1, ROOT_PW)

def solve(n, k):
    a = [1 for i in range(6)]
    res = pow_polynomial(a, n, k)
    for i in range(k - len(res)):
        res.append(0)
    return res

if __name__ == '__main__':
    n, k = map(int, input().split())
    print(*solve(n, k))