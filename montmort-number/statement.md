# Montmort Number

## Author

Kay Akashi

## Time (ms)

1000

## Memory (kb)

256000

## Difficulty

☆

## Tags

## Problem Statement 

The number of possible permutations which satisfy the following condition is called the Montmort number:

The possible number of $P = (p_1, p_2, ..., p_N)$ ( $P$ is a permutation of $(1, 2, ..., N)$ ) such that $i \neq p_i$ for $∀i ∈ (1,2,3,…,N)$.

The Montmort number for the array of length $N$ is given as:

$a_N = N! \sum_{k=2}^{N} \frac{(-1)^k}{k!}$

Given the integer $N$, output $a_N$, the Montmort number of array of length $N$.

## Constraints

$2 \leq N \leq 15$

## Input

The input consists of a single integer, $N$.

## Output

Output the Montmort number for $N$.

## Examples

### Input 

```
3
```

### Output

```
2
```

### Input

```
4
```

### Output
```
9
```