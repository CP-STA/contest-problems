def get_prime(N):
    sample = []
    for i in range(N + 1):
        sample.append(True)
    sample[0] = False
    sample[1] = False
    head = int(N ** 0.5) + 1
    for i in range(2, head + 1):
        v = 2
        while True:
            if i * v > N:
                break
            sample[i * v] = False
            v += 1
    ans = []
    for i in range(N + 1):
        if sample[i]:
            ans.append(i)
    return ans

def main():
    n = int(input())

    if n == 1:
        print()
    else:
        print(*get_prime(n))

if __name__ == '__main__':
    main()