# Within Half an Hour

## Author

Kay Akashi

## Time (ms)

1000

## Memory (kb)

256000

## Difficulty

☆☆☆☆

## Tags

## Problem Statement 

Given an underground network map consisting of $n$ stations named from $1$ to $n$, output the number of stations within $30$ minutes of walking distance from station $s$ if you choose the path optimally. 

In $m$ lines, you are given $a_i$, $b_i$, and $c_i$ $(1 \leq i \leq m)$, $(1 \leq a_i, b_i \leq n)$, $(1 \leq c_i \leq 100)$, indicating that station $a_i$ is bilaterally connected to station $b_i$ and it takes $c_i$ minute(s) to walk from one to another.

Note that, station $s$ should be counted since this can be reached in $0$ minute.

## Constraints

$1 \leq n, m \leq 1000$, $1 \leq a_i, b_i, s \leq n$, $1 \leq c_i \leq 100$.

## Input

The first line of input contains three integers, $n$, $m$, and $s$.
Following are $m$ lines each of which contains three integers, $a_i$, $b_i$, and $c_i$.

## Output

Output the answer.

## Examples

### Input

```
4 3 1
1 2 10
1 3 5
1 4 30
```

### Output

```
4
```

### Explanation

Station $1$, $2$, $3$, and $4$ can be accessed in $0$, $10$, $5$, and $30$ minutes respectively. All stations can be reached within $30$ minutes hence the answer is $4$.

### Input

```
7 5 2
2 1 19
1 3 13
1 4 9
5 4 3
6 7 10
```

### Output
```
3
```

### Explanation

Station $1$, $2$, $3$, $4$, and $5$ can be accessed in $19$, $0$, $32$, $28$, and $31$ minutes respectively. Amongst those five stations, station $1$, $2$, and $4$ satisfy the condition, hence the answer is $3$. Note that, you cannot reach station $6$ and $7$ because there's no service thus you don't count them.