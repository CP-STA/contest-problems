# Count Larger and Smaller

## Author

Kay Akashi

## Time (ms)

2000

## Memory (kb)

256000

## Difficulty

☆☆☆

## Tags

## Problem Statement 

You are given an array $a$ consisting of $n$ integers $a_{1}$, ..., $a_{n}$. Then in each of $m$ lines you are given an integer $x$ and an operation: "LARGER" or "SMALLER". If the operation is "LARGER", your task is to output the number of elements in $a$ that are STRICTLY larger than $x$. If the operation is "SMALLER", your task is to output the number of elements in $a$ that are STRICTLY smaller than $x$.

## Constraints

### Subtask 1 (.2)

$1 \leq n, m \lt 100$. Neither element in $a$ nor $x$ is smaller than $-300$ and larger than $300$.

### Subtask 2 (.8)

$100 \leq n, m \leq 10^{5}$. Neither element in $a$ nor $x$ is smaller than $-10^{5}$ and larger than $10^{5}$.

## Input

The first line of input contains one integer, $n$.
The second line contains $n$ integers that compose an array $a$.
The theird line of input contains one integer, $m$.
Following are $m$ lines each of which contains an integer $x$ and an operation which is either "LARGER" or "SMALLER".

## Output

Output the answers in $m$ lines.

## Examples

### Input

```
5
18 19 -130 6 100
4
18 LARGER
-1000 SMALLER
-300 LARGER
0 SMALLER
```

### Output

```
2
0
5
1
```