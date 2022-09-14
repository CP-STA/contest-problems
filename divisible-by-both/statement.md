# Divisible by Both

## Author

Kay Akashi

## Time (ms)

1000

## Memory (kb)

256000

## Difficulty

☆☆

## Tags

## Problem Statement 

Given integers $n$, $a$, $b$, count the number of $i$ $(1 \leq i \leq n)$ such that $i$ is divisible by both $a$ and $b$.

In the first example, set of $i$ that satisfy the condition are $12$ and $24$. Hence the answer is $2$.

In the second example, there's no $i$ that satisfies the condition whatsoever. Hence $0$.

## Constraints

$1 \leq n \leq 10^{9}$, $1 \leq a, b \leq 300$.

### Subtask 1 (.3)

$0 \leq n \lt 10^{5}$.

### Subtask 2 (.7)

$10^{5} \leq n \leq 10^{9}$.

## Input

The input contains three integers, $n$, $a$, and $b$.

## Output

Output the answer.

## Examples

### Input

```
30 3 4
```

### Output

```
2
```

### Input

```
10 9 8
```

### Output
```
0
```