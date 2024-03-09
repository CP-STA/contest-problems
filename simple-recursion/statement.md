# Simple Recursion

## Author

Kay Akashi

## Time (ms)

2000

## Memory (kb)

256000

## Difficulty

☆☆☆☆

## Tags

## Problem Statement 

Given a recursion rule $a_{n + 1} = pa_n + q$, where $a_1 = 1$, output the value of $a_X$ mod $(10^9 + 7)$ given $X$.

## Constraints

$1 \leq p, q \leq 3000$.


### Subtask 1 (.25)

$1 \leq X \leq 10^5$.

### Subtask 2 (.75)

$1 \leq X \leq 10^{12}$.

## Input

The first line of input contains $2$ integers, $p$ and $q$.
The second line of input contains $1$ integer, $X$.

## Output

Output a single integer, the value of $a_X$ mod $(10^9 + 7)$.

## Examples

### Input

```
3 4
5
```

### Output

```
241
```

### Explanation

$a_1 = 1$, $a_2 = 3 × 1 + 4 = 7$, $a_3 = 3 × 7 + 4 = 25$, $a_4 = 3 × 25 + 4 = 79$, and $a_5 = 3 × 79 + 4 = 241$.


### Input

```
2915 2999
965736817718
```

### Output
```
56311101
```