# Kay's Favourite Numbers

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

You're given an integer array $a$ consisting of $n$ distinct integers $a_{1}$, ..., $a_{n}$, Kay's favourite numbers. Then you're given an integer array $b$ consisting of integers $b_{1}$, ..., $b_{n}$. Count the number of $i$ $(1 \leq i \leq n)$ such that $b_{i}$ is one of Kay's favourite numbers.

Note that, $b$ doesn't necessarily consist of distinct integers.

## Constraints

$1 \leq n \leq 10^{5}$.

### Subtask 1 (.2)

$1 \leq n \lt 100$. No element in $a$ and $b$ is larger than $200$ and smaller than $1$.

### Subtask 2 (.8)

$100 \leq n \leq 10^{5}$. No element in $a$ and $b$ is larger than $10^{7}$ and smaller than $1$.

## Input

The first line contains one number, $n$.
The second line contains $n$ numbers, which is an array $a$.
The third line also contains $n$ numbers, which is an array $b$.

## Output

Output the answer.

## Examples

### Input 

```
3
1 7 9
4 9 9 
```

### Output

```
2
```

### Explanation

$i = 2, 3$ meet the condition since $9$ is one of Kay's favourite numbers. Hence the answer is $2$.

### Input

```
3
1 2 3
3 2 1
```

### Output
```
3
```

### Explanation

$i = 1, 2, 3$ meet the condition hence the answer is $3$.