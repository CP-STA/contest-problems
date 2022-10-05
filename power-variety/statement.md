# Power Variety

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

Given two integers $x$ and $y$, identify the name of the variable that gives the largest value: $a = x^{x}$, $b = y^{y}$, $c = x^{y}$, $d = y^{x}$. If there're multiple largest answers, print $e$ instead of answering with one of the four symbols, $a$, $b$, $c$, or $d$.

## Constraints

$1 \leq x, y \leq 5 × 10^{5}$.

## Input

The input contains two integers, $x$ and $y$ in a single line.

## Output

Output one alphabetical letter, $a$, $b$, $c$, $d$,or  $e$.

## Examples

### Input

```
3 5
```

### Output

```
b
```

### Explanation

Values of $a$, $b$, $c$, and $d$ are as follows: $27$, $3125$, $243$, and $125$. Amongst those, $b$ is apparently the largest one and there's no pair that gives identical largest value. Hence the answer is $b$.

### Input

```
1 1
```

### Output
```
e
```

### Explanation

Values of $a$, $b$, $c$, and $d$ are as follows: $1$, $1$, $1$, and $1$. In this case, $1$ is the largest value but there're multiple answers. Thus, output $e$.