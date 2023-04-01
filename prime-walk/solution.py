def prime_sieve(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return primes

n = int(input())
primes = prime_sieve(n)
ans = 0
for i in range(0, n+1):
    if primes[i]:
        ans -= i
    else:
        ans += i

print(ans)