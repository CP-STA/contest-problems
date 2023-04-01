# Prime Walk

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

You are given a positive integer, $n$. You start a game on an $x$-axis after receiving this number. 
First of all, you are standing on $x = 0$. Starting from $1$, you count the number until $n$. When you are standing at $c$ and count $i$ $(1 \leq i \leq n)$, if $i$ is not a prime number, you move rightward (hence you move from $c$ to $c + i$). If $i$ is a prime number, you move leftward (hence you move from $c$ to $c - i$). After completing this game, where will you be?

Note that, $1$ is NOT a prime number.

## Constraints

$1 \leq n \leq 10^{4}$.

### Subtask 1 (.2)

$1 \leq n \lt 100$.

### Subtask 2 (.8)

$100 \leq n \leq 10^{4}$.

## Input

The input consists of one number, $n$.

## Output

Output the answer.

## Examples

### Input 

```
5
```

### Output

```
-5
```

### Explanation

You are firstly at $x = 0$. Then, you move in a following way: $0 → 1 → -1 → -4 → 0 → -5$.

### Input

```
200
```

### Output
```
11646
```