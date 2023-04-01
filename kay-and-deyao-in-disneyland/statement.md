# Kay and Deyao in Disneyland

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

Anurag, who is our Sponsorship Coordinator, is today a Disneyland Trip Coordinator. He's taking CPSTA's committee members to Disneyland Paris. However, a couple of days before the departure, Kay and Deyao had a serious quarrel over the unsolved conundrum disputed across the UK; "When putting the clotted cream and jam on the scone, which should be spread first?". The argument did not reach a concordance until the trip to Paris, and in order to sidestep further development of their adverse relationship, Anurag now needs to plan the Disneyland trip accordingly.

Disneyland Paris consists of $N$ attractions with names $1$, ..., $N$. Also, there're $(N - 1)$ undirected paths that connect two attractions; attraction $A_i$ and $B_i$ are bilaterally connected, and the distance between $A_i$ and $B_i$ is $C_i$ $(1 \leq i \leq N - 1)$. In this theme park, it is ensured that you can reach one attraction from another attraction ($i.e.$ There's no "isolated" attraction whatsoever, and the theme park itself is not disjointed). 

Now, although expecting that the relationship between Kay and Deyao is to be gradually restored as time goes by, Anurag wants to start the trip by dividing them into two separate groups, and make them start at two attractions which are most distant from each other, so that he feels the least awkward. To be more precise, Anurag wants to select two attractions in such a way that the shortest path between two is maximised. Anurag wants to know that maximal distance he can choose in Disneyland Paris. Output this distance.


## Constraints

$1 \leq C_i \leq 100$ $(1 \leq i \leq N - 1)$.

### Subtask 1 (.2)

$2 \leq N \leq 50$.

### Subtask 2 (.8)

$2 \leq N \leq 5000$.

## Input

In the first line of input, you're given $N$, the number of attractions in Disneyland in Paris.
Following are $(N - 1)$ lines, each of which consists of three numbers, $A_i$, $B_i$, and $C_i$.

## Output

Output the answer in a single line.

## Examples

### Input 

```
5
1 2 11
1 3 6
3 4 2
3 5 6
```

### Output

```
23
```

### Explanation

If Anurag chooses attraction $2$ and $5$, the length of shortest path is $6 + 6 + 11 = 23$ and this is the maximum he can get.

### Input 

```
30
20 24 45
28 2 92
28 3 15
14 4 89
5 11 15
16 8 31
27 9 24
17 20 3
15 18 99
6 22 75
18 26 4
11 21 86
30 15 65
8 6 5
15 28 46
25 16 60
15 14 13
6 10 1
24 7 62
20 27 83
25 30 12
24 23 79
30 5 2
20 12 3
20 29 80
25 17 20
6 13 12
15 1 11
30 19 63
```

### Output

```
386
```