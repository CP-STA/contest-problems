# Clinical Tutorial Groups

## Author

Kay Akashi

## Time (ms)

2000

## Memory (kb)

256000

## Difficulty

☆☆☆

## Tags

## Problem Statement 

Students in the School of Medicine are divided into several small clinical tutorial groups for clinical skills teaching. The groups are shuffled every year.

There're $N$ students in the School. You're given information as to "who was with who" as $M_{1}$ pairs last year. Then, you're also given the same information of $M_{2}$ pairs this year. Be noted that these information do not give you comprehensive lists of pairs (i.e. $M_{1}, M_{2} \leq \frac{N(N - 1)}{2}$).

Amongst $M_{2}$ pairs of clinical groups allocation this year, how many of them were the pairs of two students who were in the same group last year, according to the provided information?

Students are denoted as numbers $1$, $2$, ..., $N$. Suppose that there was no student who was added to or left the class during the transition of those two academic years.
 
## Constraints

$2 \leq N, M_{1}, M_{2} \leq 10^{5}$

## Input

The first line of input is a single integer, $N$.
The second line is a single integer, $M_{1}$.
Then, $M_{1}$ lines follow, each of each is shown by $p$ and $q$ ($1 \leq p, q \leq N$, $p \neq q$) separated by a single blank space, indicating student $p$ and $q$ were in the same group last year.
The ($M_{1} + 3$)-th line of input is a single integer, $M_{2}$.
Then, $M_{2}$ lines follow, each of each is shown by $p$ and $q$ ($1 \leq p, q \leq N$, $p \neq q$) separated by a single blank space, indicating student $p$ and $q$ are in the same group this year.

## Output

Answer the number of pairs amongst last $M_{2}$ lines two of which were in the same group last year as well.

## Examples

### Input

```
6
6
1 2
2 5
5 2
3 4
4 6
6 3
4
3 1 
6 4
2 3 
1 2
```

### Output

```
2
```

### Explanation

$6$ students are divided into $2$ groups.
Last year, Group $1$ had students $1$, $2$, and $5$. Group $2$ had students $3$, $4$, and $6$.
Now looking at this year's allocation, students $1$ and $3$ were not in the same group, so it doesn't add to the answer.
Students $6$ and $4$ were both in the Group $2$ last year, so there's one pair so far. 
Student $2$ was in Group $1$ while student $3$ was in Group $2$, so not same.
Students $1$ and $2$ were both in Group $1$, so it counts.
Thus, the total number of pairs questioned is $2$.


### Input

```
7
3
1 3
3 4
2 5
5
1 4
6 7
7 5
5 2
5 3
```

### Output
```
2
```

### Explanation

In the first query, note that the pair information of students $1$ and $4$ was not directly mentioned in the first $M_{1}$ queries, but they were in the same group last year. Thus it counts.
In the second query, students $6$ and $7$ may have been in the same group last year, but since we don't have explicit evidence, it doesn't contribute to the final answer.
In the third query, again any information about student $6$ is unavailable, so we don't count it.

### Input

```
10
6
4 9
10 9
3 8
3 5
7 5
2 6
3
1 7
7 8
2 4
```

### Output
```
1
```
