# Mozart Index

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

All the beautiful compositions of Wolfgang Amadeus Mozart ($1756$-$1791$) are chronologically contained in what is known as a "Köchel catalogue". In Köchel catalogue, each piece he composed is assigned an index from $1$ to $626$ (the first piece is a harpsichord piece Mozart in his childhood composed, and the last piece is the incomplete requiem). For example, K.$331$ is his Piano Sonata No.$11$, and its third movement is well-known for its name "Turkish March" (Alla Turca). By the way, the problem writer is now practicing its first movement, "Andante Grazioso", and is performing it with some other French Suite pieces by Bach at the end-of-semester recital (Solo Music St Andrews, $19:00$ at Gifford Room, Laidlaw Music Centre), so please let me know if anyone is ever interested, at ka203@st-andrews.ac.uk or on my Instagram: @kay.liechtenstein .

Going back to the problem, it is known that we can roughly esimate how old Mozart was when he composed a piece by having a look at its Köchel index. That is, divide the index by $25$, and then add $10$ to it. 

Let's take my top favourite piece Piano Concerto No.$22$ as an example. Its Köchel index is K.$482$. Thus, rough estimation of his age at the time of composition is $482 / 25 + 10 = 29.28$. Actually, this concerto was known to be composed at the age of $29$ in Vienna. Pretty good estimator, although it does not work very well occasionally. 

In this problem, you are required to output the estimated age of Mozart given a Köchel index $N$ as an input. Note that, you are also required to round an answer down so that it is reported as an integer. 

## Constraints

$1 \leq N \leq 626$.

## Input

You are given $N$ in a single line.

## Output

Output estimated Mozart's age at the time of composition of K.$N$, which is rounded down and reported as an integer.

## Examples

### Input

```
265
```

### Output

```
20
```

### Explanation

K.$265$ is the "Twelve Variations in C Major" (a.k.a. "Twinkle Twinkle Little Star"), and this was composed when he was actually $25$ in Vienna. On the other hand, calculation shows $265 / 25 + 10 = 20.6$. Not very accurate, but it still works.

### Input

```
626
```

### Output
```
35
```

### Explanation

This is his incomplete requiem, "Requiem in D minor". $626 / 25 + 10 = 35.04$ and the output is $35$ since you round it down. For your information, Mozart died at the age of $35$. 