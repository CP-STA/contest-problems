from solution import solve
import random
import json

def generate_test_case(level, full=False, seed=42):
    rng = random.Random(seed)
    N = 2**level

    translation_map = list(range(N))
    rng.shuffle(translation_map)

    pairs = []
    for i in range(level):
        group_size = 2**(level-i)
        for j in range(2**i):
            pairs.append((N//(2 ** (i+1))-1 + j * group_size, N//(2 ** (i+1)) + j * group_size))
    pairs = list(reversed(pairs))
    if not full:
        remaining = sample_sorted(rng, pairs, N - min(N-1, 4))
    else:
        remaining = pairs
    remaining_traslated = [(translation_map[i], translation_map[j]) for i, j in remaining]
    return remaining_traslated


def sample_sorted(rng, l, N):
    sorted_sample = [
        l[i] for i in sorted(rng.sample(range(len(l)), N))
    ]
    return sorted_sample

def generate_pairs(population_size, n_pairs, seed=42):
    rng = random.Random(seed)
    pairs = []
    for _ in range(n_pairs):
        id = random.randrange(population_size ** 2)
        i = id % population_size
        j = id // population_size
        pairs.append((i, j))
    return pairs

def main():
    rng = random.Random(42)
    test_cases = []
    for i in range(2):
        modify = generate_test_case(16, full=True, seed=rng.randrange(2**31))
        query = generate_pairs(2**16, 10**5)
        solution = solve(2**16, modify, query)
        new_case = {
            'input': '\n'.join([
                f'{2**16}',
                f'{len(modify)}',
                *[f'{i+1} {j+1}' for i, j in modify],
                f'{len(query)}',
                *[f'{i+1} {j+1}' for i, j in query],
            ]),
            'output': f'{solution}',
        }
        test_cases.append(new_case)
    for i in range(3):
        modify = generate_test_case(16, full=False, seed=rng.randrange(2**31))
        query = generate_pairs(2**16, 10**5, seed=rng.randrange(2**31))
        solution = solve(2**16, modify, query)
        test_cases.append({
            'input': '\n'.join([
                f'{2**16}',
                f'{len(modify)}',
                *[f'{i+1} {j+1}' for i, j in modify],
                f'{len(query)}',
                *[f'{i+1} {j+1}' for i, j in query],
            ]),
            'output': f'{solution}',
        })
    print(json.dumps(test_cases, indent=2))


if __name__ == "__main__":
    main()
