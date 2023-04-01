import json
import random
from math import floor

def main():
    test_cases = []
    for _ in range(80):

        N = random.randint(1, 626)
        IN = str(N) + '\n'

        age = floor(N / 25 + 10)
        OUT = str(age) + '\n'

        test_cases.append({
        "input": f"{IN}",
        "output": f"{OUT}"
        })

    print(json.dumps(test_cases, indent = 2))


if __name__ == '__main__':
    main()