# String Quartet

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

Kay has $4$ strings and lays them on an X-axis. String $i$ has its left end at $x = l_i$ and right end at $x = r_i$. Now, find the length of line segment where all the $4$ strings are laid. 

## Constraints

$0 \leq l_i \lt r_i \leq 10$.

All the input values are given as integers.

## Input

The input contains $4$ lines, each of which has $l_i$ and $r_i$.

## Output

Output a single integer, the length of line segment where all $4$ strings overlap.

## Examples

### Input

```
0 8
3 10
5 8
1 9
```

### Output

```
3
```

### Explanation

It is the line segment between $x = 5$ and $x = 8$ that satisfies the condition. Hence the length is $8 - 5 = 3$.


### Input

```
0 3
0 3
3 6
3 6
```

### Output
```
0
```

### Explanation

$x = 3$ satisfies the condition. However, note that the point has a length of $0$.

### Input

```
0 1
2 3
4 5
6 7
```

### Output
```
0
```
