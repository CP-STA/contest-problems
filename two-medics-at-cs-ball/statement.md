# Two Medics at CS Ball

## Author

Kay Akashi

## Time (ms)

3000

## Memory (kb)

256000

## Difficulty

☆☆☆

## Tags

## Problem Statement 

Kay is an introvert. However, he determined to make new friends. Thus, he's bought a ticket for Computer Science Ball happening soon, although he's not a CS student.

But Kay is an introvert. Because he's too frightened to go there by himself, he asked his friend Liana in his medicine class to join him. 

Now Kay and Liana are in the ball venue. It looks like $N$ CS students are there, meaning there're $N + 2$ people there in total.

But Kay is an introvert. He ends up with talking only to Liana and never tries to socialise with others at all. Moreover, he's feeling annoyed (*how selfish he is!*) when a pair of two CS students is standing in a way that the line segment between them intersects with that between Kay and Liana. Note that, Kay is such a selfish person who also gets annoyed when at least one person of the pair is standing on the line segment betweek Kay and Liana. Also, he gets annoyed when either Kay or Liana is on the line segment between a pair of two CS students.

The venue is expressed as a two-dimensional graph with x and y-axes. Everyone's locations have non-negative integer values on both x and y-axes. Kay is standing at ($K_x, K_y$), Liana is standing at ($L_x, L_y$). Other $N$ CS students are standing at ($X_i$, $Y_i$) ($1 \leq i \leq N$). Your task is to count the number of pairs that annoy miserable Kay.

## Constraints

$1 \leq N \leq 200$.
$0 \leq K_x, K_y, L_x, L_y, X_i, Y_i \leq 500$. All the locations are provided as integers.

## Input

The first line of input contains a single integer $N$, the number of CS students joining the ball.
The second line of input contains $4$ integers, $K_x$, $K_y$, $L_x$, and $L_y$, locations of Kay and Liana.
Then, $N$ lines follow, each of which contains $2$ integers, $X_i$ and $Y_i$, the location of student $i$. 

It is ensured that no two persons are standing at the exact same location.

## Output

Output a single integer, the number of pairs that annoy Kay.

## Examples

### Input

```
4
3 0 3 3
0 0
100 101
6 4
100 100
```

### Output

```
2
```

### Explanation

Student $1$ and $3$ are annoying Kay, because the line segment between them intersects with that between Kay and Liana at ($x$, $y$) = ($3$, $2$). Also, student $1$ and $4$ are annoying Kay because Liana is standing between them. No other pair annoys Kay, so output $2$, the total number of annoying pairs to Kay.


### Input

```
1
28 83 74 92
64 73
```

### Output
```
0
```

### Explanation

No matter where the CS student is standing, Kay never gets annoyed because there's no "pair" of CS students who can annoy him. In such a case, output $0$. 

### Input

```
2
3 0 3 3
0 0
1 1
```

### Output
```
0
```

### Explanation

Note that, student $1$ and $2$ are **not** annoying Kay at all in this scenario.

### Input

```
15
245 61 115 444
345 134
3 131
74 99
234 339
89 77
10 10
75 75
92 111
111 500
88 290
72 73
77 11
0 88
66 91
111 300
```

### Output
```
24
```
