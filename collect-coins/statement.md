# Collect Coins

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

You're playing a game that is composed of $n$ rounds. Before starting a game, you have $0$ coin. In $i$-th round, you earn $A[i]$ coins. However, the maximum number of coins you can have is $10$ and minimum is $0$ ($i.e.$ you will not have more than $10$ coins, and you will not have less than $0$ coin). What is the resulting number of coins you have after finishing all $n$ rounds?

Note that, $A[i]$ can be negative: in this case, you lose $A[i]$ coins rather than earning them.

## Constraints

$0 \leq n \lt 10^{5}$, $-5 \leq A[i] \leq 5$.

## Input

The first line of input contains one integer, $n$.
The second line of input contains $n$ integers, $A[i]$.

## Output

Output the answer.

## Examples

### Input

```
4
3 5 5 -3
```

### Output

```
7
```

### Explanation

The numbers of coins you have after finishing each round are as follows: $3$, $8$, $10$, and $7$, hence the answer is $7$.

### Input

```
3
2 -4 -4
```

### Output
```
0
```

### Explanation

The numbers of coins you have after finishing each round are as follows: $2$, $0$, and $0$ hence the answer is $0$.