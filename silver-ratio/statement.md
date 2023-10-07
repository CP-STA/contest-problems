# Silver Ratio

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

You will think of a recursion $a_{n + 2} = pa_{n + 1} + qa_{n}$ $(a_{1} = 1, a_{2} = 1)$.

Given integers $q$ and $d$, find $p$ such that $\lim_{n \to \infty} (\frac{a_{n + 1}}{a_{n}}) = d$. In output, round $p$ to the nearest integer. 

## Constraints

$1 \leq q, d \leq 1000$.

## Input

The input consists of two integers, $q$ and $d$.

## Output

Output the answer. Make sure the answer is rounded to the nearest integer.

## Examples

### Input

```
33 972
```

### Output

```
972
```

### Input

```
891 533
```

### Output
```
531
```
