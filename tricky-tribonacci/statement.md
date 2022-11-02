# Tricky Tribonacci

## Author

Kay Akashi

## Time (ms)

1000

## Memory (kb)

256000

## Difficulty

☆☆☆☆☆

## Tags

## Problem Statement 

Sequence $a$ meets the following recursion: $a_{n + 3} = pa_{n + 2} + qa_{n + 1} + ra_{n}$. Provided that $a_{1} = x, a_{2} = y$, and $a_{3} = z$, your task is to output the value of $a_{k}$. However, because the answer can become astronomically large, you are required to output $a_{k}$ mod $10^{9} + 7$. In other word, output the remainder of $a_{k}$ divided by $10^{9} + 7$.

## Constraints

$1 \leq p, q, r, x, y, z \leq 10^{5}$, $1 \leq k \leq 10^{12}$.

## Input

The first line of input contains three integers, $p$, $q$, and $r$.
The second line of input contains three integers, $x$, $y$, and $z$.
The third line of input contains one integer, $k$.

## Output

Output the answer.

## Examples

### Input
```
1 4 9
3 2 7
4
```

### Output
```
42
```

### Explanation
In this case $a_1 = 1, a_2 = 4, a_3 = 9$, so $a_4 = 3a_3 + 2a_2 + 7a_1 = 42$.

### Input

```
1 1 1
1 1 1
40
```

### Output

```
129195424
```

### Input

```
13238 91313 41471
12374 58241 31231
831487118462
```

### Output
```
102645325
```