# Array Convergence

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

Given an array consisting of $n$ integers $a_{1}$, ..., $a_{n}$, you can do a following operation to each element only once:
choose any integer $x$ $(-k \leq x \leq k)$ and add $x$ to an element.

As a result of performing the operations to all the elements in the array, can you make all the elements equivalent?

## Constraints

$1 \leq n \leq 10^{4}$, $1 \leq k \leq 2 × 10^{4}$, $-10^{4} \leq a_i \leq 10^{4} (1 \leq i \leq n)$.

## Input

The first line of input contains two integers, $n$ and $k$.
The second line of input contains $n$ integers that form an array $a$.

## Output

Output "Yes" if you can make all the elements of $a$ equivalent. Otherwise, output "No".

## Examples

### Input

```
5 2
-1 3 2 2 0
```

### Output

```
Yes
```

### Explanation

You can create the new array by adding following numbers to each element respectively: $(2, -2, -1, -1, 1)$. As a result of those operations, the new array consists of $1$ only and the goal is achieved. Hence the answer is "Yes".

### Input

```
4 1
-83 -10 910 23
```

### Output
```
No
```