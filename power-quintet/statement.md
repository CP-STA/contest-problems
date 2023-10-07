# Power Quintet

## Author

Kay Akashi

## Time (ms)

1000

## Memory (kb)

256000

## Difficulty

☆

## Tags

## Problem Statement 

Given an integer $N$, judge if there's any combination of $5$ non-negative integers $(a, b, c, d, e)$ such that $a^{a} + b^{b} + c^{c} + d^{d} + e^{e} = N$. 

## Constraints

$0 \leq N \leq 10^{5}$.

## Input

The input consists of a single integer, $N$.

## Output

If there's any combination that satisfies the outlined condition, output "Yes". Otherwise, "No" (case-specific).

## Examples

### Input

```
3410
```

### Output

```
Yes
```

### Explanation

$(a, b, c, d, e) = (3, 1, 4, 1, 5)$ satisfies the condition.

### Input

```
0
```

### Output
```
No
```

### Explanation
Be noted that if $(a, b, c, d, e) = (0, 0, 0, 0, 0)$ the resulting value is $5$.