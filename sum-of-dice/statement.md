# Sum of Dice

## Author
Deyao Chen

## Time (ms)

10000

## Memory (kb)

256000

## Difficulty

☆☆☆☆☆

## Tags

## Problem Statement

You throw a special programmers' die, which has $6$ faces with $0$, $1$, $2$, $3$, $4$, or $5$ dots, $n$ times. In how many different ways can the sum of all the throws be $s$, for all $s$ from $0$ to $k - 1$? Since the answer can be astronomically large, output the remainder of each number divided by $7340033$.

## Constraints

$1 \le n \le 10^{5}$ and $1 \le k \le 10^{4}$

### Subtask 1 (.1)

$1 \le n \le 9$ 

### Subtask 2 (.1)

$k - n \le 5$

### Subtask 3 (.2)

$1 \le n \le 10$ and $1 \le k \le 300$

### Subtask 4 (.1)

$1 \le k \le 300$ 

### Subtask 5 (.5)

No more constraints.


## Input

Input consists of a line containing $n$ and $k$, separated by a space.

## Output

Output a list of numbers, separated by a space which is the different ways in which the sum of all the throws become $0, 1, 2, 3, ..., \text{or}, k-1$, respectively. 

## Examples

### Input

```
1 10
```

### Output

```
1 1 1 1 1 1 0 0 0 0
```

### Explanation

Since you only throw the dice once, there is only $1$ way to make the sum $0$, $1$, ..., or $5$ and $0$ way to make anything larger than $5$. 

### Input

```
3 17
```

### Output 

```
1 3 6 10 15 21 25 27 27 25 21 15 10 6 3 1 0
```

### Explanation

Since you throw it three times, there are $3$ ways to get a sum of $1$, $6$ ways to get a sum of $2$ and $27$ ways to get a sum of $7$.