# Tokyo Exploration

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

Tokyo is a wonderland of gastronomy.

There're $N$ sushi places and $M$ ramen places in one area of Tokyo. $i$-th sushi place costs you $A_i$ yen ($1 \leq i \leq N$) and $j$-th ramen place costs you $B_j$ yen ($1 \leq j \leq M$) (note: yen is a Japanese currency). 

You decided to go to one sushi restaurant for lunch and one ramen restaurant for dinner. Given an integer $K$ ($1 \leq K \leq N + M$), output the $K$-th biggest price you're going to spend in total. More formally, output the $K$-th greatest value of $A_i + B_j$ where $1 \leq i \leq N$ and $1 \leq j \leq M$.

## Constraints

$1 \leq K \leq N + M$. $1 \leq A_i, B_j \leq 10^9$. 


### Subtask 1 (.25)

$1 \leq N, M \leq 100$.

### Subtask 2 (.75)

$1 \leq N, M \leq 10^5$.

## Input

The first line of input contains $3$ integers, $N$, $M$, and $K$.
The second line of input contains $N$ integers, $A_1$, $A_2$, ..., $A_N$.
The third line of input contains $M$ integers, $B_1$, $B_2$, ..., $B_M$.

## Output

Output a single integer, the $K$-th biggest total price of sushi lunch and ramen dinner.

## Examples

### Input

```
3 3 5
1200 1500 1000
800 1100 1700
```

### Output

```
2300
```

### Explanation

From the most expensive to cheapest, possible combined prices are as follows: $3200, 2900, 2700, 2600, 2300, 2300, 2100, 2000, 1800$. The $5$-th most expensive combination is $2300$ yen. 


### Input

```
7 5 12
1234 2342 8255 9273 1400 988 1482
3002 2351 1925 1351 1000
```

### Output
```
4693
```