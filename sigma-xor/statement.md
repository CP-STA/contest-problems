# Sigma XOR

## Author

Kay Akashi

## Time (ms)

1000

## Memory (kb)

256000

## Difficulty

☆☆☆

## Tags

## Problem Statement 

Given a positive integer $N$, answer the value of $1 ⊕ 2 ⊕ ... ⊕ N$, where $⊕$ signifies XOR operation.

Note that, in XOR operation of two integers, each bit of two integers in binary format is calculated in the following manner: $0 ⊕ 0 = 0$, $0 ⊕ 1 = 1$, $1 ⊕ 0 = 1$, $1 ⊕ 1 = 0$. For example, $12_{(10)} ⊕ 34_{(10)} = 001100_{(2)} ⊕ 100010_{(2)} = 101110_{(2)} = 46_{(10)}$. 

## Constraints

$1 \leq N \leq 10^{15}$.

### Subtask 1 (.2)

$1 \leq N \lt 10^{5}$.

### Subtask 2 (.8)

$10^{5} \leq N \leq 10^{15}$.

## Input

The input consists of one integer, $N$.

## Output

Output the answer.

## Examples

### Input

```
14
```

### Output

```
15
```

### Explanation

$1 ⊕ 2 ⊕ ... ⊕ 14 = 15$.

### Input

```
1
```

### Output
```
1
```

### Explanation

Note that when $N = 1$ we do not perform any operation.

### Input

```
392857971529353
```

### Output
```
1
```

### Explanation

May I please skip the explanation for this.