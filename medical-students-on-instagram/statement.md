# Medical Students on Instagram

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

There're $N$ students on Instagram in the University. Students are numbered from $1$ to $N$. Kay is curious about how close medical students are with other people in the University on Instagram, so he's going to conduct a brief research, looking at $C$ students from medical school.

Medical students are numbered $P_{1}, ..., P_{C}$. According to the statistics, there're $M$ mutual connections in total, and student $x_{i}$ and $y_{i}$ ($1 \leq i \leq M, 1 \leq x_{i}, y_{i} \leq N$) are following each other. Considering these connections as a network, Kay defined "distance" between two users as the minimal number of connections from one to reach the other. Distance between one user and him/herself is defined $0$.

Kay wants to know, for each student $i$ in the University, the minimum possible distance between student $i$ and $m$ ($m ∈ P$) in the University. If student $i$ is a medical student, output $0$. If there's neither direct nor indirect connection between student $i$ and any medical student, output $-1$.

## Constraints

$2 \leq N \leq 4 × 10^{5}$. $1 \leq M \leq 10^{5}$.

$1 \leq C \leq N$.

### Subtask 1 (.2)

$2 \leq N \leq 100$

### Subtask 2 (.8)

$2 \leq N \leq 4 × 10^{5}$.

## Input

The first line of input contains three integers, $N$, $M$, and $C$.
The second line contains $C$ numbers, $P_{1}, ..., P_{C}$.
Then, $M$ lines follow, each of which consists of two integers, $x_{i}$ and $y_{i}$.
It is guaranteed that one pair of connection appears in the input no more than twice.

## Output

Output the answers in a single line, separated by a single space.

## Examples

### Input 

```
10 8 3
1 9 4
1 2
1 7
3 9
3 4
3 6
4 5
4 6
6 8
```

### Output

```
0 1 1 0 1 1 1 2 0 -1
```

### Explanation

For example, from the perspective of student $8$, distance between him and medical student $1$ can be considered infinitely large. Between $8$ and medical student $9$, the distance is $3$. Between student $8$ and medical student $4$, the distance is $2$. Thus, the answer is $2$ for student $8$.

### Input

```
6 6 3
1 2 3
1 2
2 3
3 1
4 5
5 6
6 4
```

### Output
```
0 0 0 -1 -1 -1
```

### Explanation

Students $4$, $5$, and $6$ cannot reach any medical student whatsoever. In that case, output $-1$.
