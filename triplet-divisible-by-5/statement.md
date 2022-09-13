# Triplets Divisible by 5

## Author

Kay Akashi

## Time (ms)

1000

## Memory (kb)

256000

## Difficulty

☆☆☆

## Tags

## Problem Statement 

You are given a list of non-negative numbers, $a_1, a_2, a_3, ..., a_n$. You want to choose $i$, $j$, $k$ $(1 \leq i \lt j \lt k \leq n)$ in such a way that $a_i + a_j + a_k$ is divisible by $5$. How many possible pairs of $(i, j, k)$ are there in total?

In the first example, $(1, 2, 3)$ is the only set of indices that satisfies the condition. Hence the answer is $1$.

In the second example, $(1, 2, 3)$, $(1, 2, 4)$, $(1, 3, 5)$, and $(1, 4, 5)$ satisfy the condition. Hence the answer is $4$.

## Constraints

$3 \leq n \leq 10^{5}$, 
$0 \leq a_i \leq 10^{5}$ $(1 \leq i \leq n)$.

### Subtask 1 (.2)

$3 \leq n \lt 100$.

### Subtask 2 (.8)

$100 \leq n \leq 10^{5}$.

## Input

The first line contains one number $n$, the length of $a$.
Following is the sequence of $n$ numbers, separated by single spaces, that compose $a$.

## Output

Output the answer.

## Examples

### Input 

```
3
0 5 10
```

### Output

```
1
```

### Input

```
5
2 3 0 10 8
```

### Output
```
4
```