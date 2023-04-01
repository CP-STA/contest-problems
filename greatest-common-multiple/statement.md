# Greatest Common Multiple

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

Given an integer $X$ and $n$ integers $a_{1}$, ..., $a_{n}$, find the greatest common multiple of all the elements in $a$ which is smaller than or equal to $X$. If there is no such answer, output $-1$ instead.

Note that, common multiple of $a$ is the number which can be divided by any element in $a$. Your task is to find the greatest one amongst several possible (or zero) common multiples.

## Constraints

$1 \leq n \leq 50$, $1 \leq a_i \leq 100$ $(1 \leq i \leq n)$, $1 \leq X \leq 10^{9}$.

## Input

The first line of input contains two integers, $n$ and $X$.
The second line contains $n$ integers separated by single spaces in between.


## Output

Output the answer. 

## Examples

### Input

```
3 100
2 3 5
```

### Output

```
90
```

### Explanation

In this example, common multiples of $a$ which are smaller than or equal to $X = 100$ are $(30, 60, 90)$. The greatest common multiple of $a$ here is therefore $90$.

### Input

```
4 10
2 5 8 9
```

### Output
```
-1
```

### Explanation

In this example, the least common multiple is $360$. This indicates that there's no common multiple that is smaller than or equal to $10$. For this reason, output $-1$. 