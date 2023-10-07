# f Naturaliser

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

Given $6$ positive integers $a_{1}$, $b_{1}$, $c_{1}$, $a_{2}$, $b_{2}$, and $c_{2}$, you will think of a function $f(x) = \frac{a_{1}x^{2} + b_{1}x + c_{1}}{a_{2}x^{2} + b_{2}x + c_{2}}$.

Your task is to find all $x$ such that $f(x)$ is a positive integer. ($x$ is an integer). 0 is not a positive integer.

It is ensured that $a_{1} \lt a_{2}$.

## Constraints

$1 \leq a_{1}, b_{1}, c_{1}, a_{2}, b_{2}, c_{2}, \leq 10$.
$a_{1} \lt a_{2}$.

## Input

The input consists of 6 integers, $a_{1}$, $b_{1}$, $c_{1}$, $a_{2}$, $b_{2}$, and $c_{2}$, in a single line.

## Output

List the possible $x$ in one line, in an **increasing** order. If there's no such $x$, output "None" instead.

## Examples

### Input

```
3 5 8 4 9 3
```

### Output

```
-5 -2 1
```

### Explanation

$f(x) = \frac{3x^{2} + 5x + 8}{4x^{2} + 9x + 3}$.
$f(-5) = 1$, $f(-2) = 10$, and $f(1) = 2$. No other value satisfies the condition.

### Input

```
3 3 2 4 3 2
```

### Output
```
0
```

### Explanation

It is only $x = 0$ that makes $f(x)$ a positive integer, which is $1$.

### Input

```
3 3 5 4 5 7
```

### Output
```
None
```

### Explanation

Be aware that some types of $f(x)$ don't have any $x$ that makes it a positive integer number. In this case, output "None".
