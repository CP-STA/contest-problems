# Concert Organiser

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

Kay and Alden are organising a classical music concert. 

Kay is in charge of organising a concert venue, and Alden is in charge of creating a programme. There're $N$ pieces being performed in the concert, and in determining the order of the pieces, he asks Kay if he has any preference over the order, and Kay said he wants the piece $p_{i}$ to be performed before piece $q_{i}$ ($1 \leq i \leq M$).

Can Alden create a programme that follows all of Kay's $M$ requests?

## Constraints

$2 \leq N, M \leq 10^{5}$.
$1 \leq p_{i}, q_{i} \leq N$ ($p_{i} ≠ q_{i}$).

## Input

The first line of input consists of two integers, $N$ and $M$.
Then, $M$ lines follow, each of which consists of two integers, $p_{i}$ and $q_{i}$.

## Output

If Alden is able to create a programme that completely agrees with $M$ requests by Kay, output "Yes". Otherwise, "No".

## Examples

### Input

```
5 5
4 3
4 5
4 2
2 1
1 5
```

### Output

```
Yes
```

### Explanation

If the order of pieces is $4 → 2 → 3 → 1 → 5$, all the requests are satisfied.

### Input

```
4 4
1 2
2 3
3 4
4 1
```

### Output
```
No
```

### Explanation

$4$ conditions cannot be satisfied simultaneously. 