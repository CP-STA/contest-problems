import json
import random

def solve(N, T, W):
    dp = []
    for i in range(N + 1):
        li = [float('inf') for i in range(T + 1)]
        dp.append(li)
    dp[0][0] = 0
    for i in range(N):
        for j in range(T + 1):
            if j - W[i] >= 0:
                dp[i + 1][j] = min(dp[i][j], dp[i][j - W[i]] + 1)
            else:
                dp[i + 1][j] = dp[i][j]
    if dp[N][T] != float('inf'):
        return str(dp[N][T])
    else:
        return '-1'

def main():
    test_cases = []
    for _ in range(40):
        N = random.randint(1, 10)
        T = random.randint(1, 700)
        W = []
        for i in range(N):
            x = random.randint(1, 99)
            if x != T:
                W.append(x)
            else:
                W.append(x + 1)

        OUT = solve(N, T, W)

        W = [str(w) for w in W]

        IN = str(N) + ' ' + str(T) + '\n' + ' '.join(W)

        test_cases.append({
        "input": f"{IN}",
        "output": f"{OUT}",
        "subtask": 1
        })
    for _ in range(100):
        N = random.randint(1, 100)
        T = random.randint(1, 10000)
        W = [random.randint(1, 100) for i in range(N)]

        OUT = solve(N, T, W)

        W = [str(w) for w in W]

        IN = str(N) + ' ' + str(T) + '\n' + ' '.join(W)

        test_cases.append({
        "input": f"{IN}",
        "output": f"{OUT}",
        "subtask": 2
        })


    print(json.dumps(test_cases, indent = 2))


if __name__ == '__main__':
    main()