# EZ Bar

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

In order to strengthen his biceps brachii muscles, Kay is coming to the gym today. Kay now wants to use an EZ bar, a wavy bar to whose right and left ends he can add some weights. He holds this bar with both his arms, and flexes arms to build his muscles.

Today he wants to make the total weight $2T$ kg. Luckily, he has found one weight of $T$ kg for the left end immediately. However, it seems that other $T$ kg weights are all unavailable, hence he needs to take several other available weights so that the total weight for the right end becomes $T$ kg too. In choosing weights, he wants to minimise the number of weights he has to take because he is too lazy to walk back and forth. Being horrible at maths, he asks his smart friend Alden to calculate the minimal number of weights he needs to take to make the total weight for the right end exactly $T$ kg. Report his answer.

Available weights are given as $W$ which is a single sequence of length $N$; $W_1$, ..., $W_N$.

Also, if it's impossible to make $T$ kg out of $W$, output $-1$ instead.

## Constraints

$1 \leq N \leq 100$, $1 \leq W_i \leq 100$, $0 \leq T \leq 10^{4}$.
There's no $i$ such that $W_i = T$ $(1 \leq i \leq N)$.

### Subtask 1 (.2)

$1 \leq N \leq 10$.

### Subtask 2 (.8)

$1 \leq N \leq 100$.

## Input

The first line of input contains two integers, $N$, $T$.
The second line of input contains $N$ integers, $W_i$ $(1 \leq i \leq N)$.

## Output

Output an answer in a single line.

## Examples

### Input 

```
5 16
2 4 4 8 10
```

### Output

```
3
```

### Explanation

One example of the solution is to pick up $W_2$, $W_3$, and $W_4$. Another example is to pick up $W_1$, $W_2$, and $W_5$. However, because there's no way to make $16$ by picking up only $2$ or $1$ elements, the minimal number of weights Kay needs to take is $3$.


### Input 

```
4 20
1 10 18 11
```

### Output

```
-1
```

### Explanation

Even Alden cannot find a set of weights to make $T$ kg out of this sequence. Thus, the answer is $-1$.