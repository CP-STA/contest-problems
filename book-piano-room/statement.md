# Book Piano Room

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

In the Music Centre, there is only one piano practice room. There are $n$ time slots in a single day available for the piano practice room.

One person is permitted to book several time slots in a day. The rule for booking is that, one firstly chooses consecutive time slots, and he/she can use practice rooms during those time slots where there's no preexisting booking.

Students and teaching staff love playing the piano, and today $m$ people are trying to book piano rooms. It is known that $i$-th person $(1 \leq i \leq m)$ would like to book a room between $l_{i}$-th time slot and $r_{i}$-th time slot inclusive. 

Your task is to output the number of time slots in which the practice room is vacant.

Note that, $i$-th person can make bookings earlier than $(i + 1)$-th person does $(1 \leq i \leq n - 1)$.

## Constraints

$1 \leq n, m \leq 10^{5}$, $1 \leq l \leq r \leq n$.

### Subtask 1 (.2)

$1 \leq n, m \lt 100$.

### Subtask 2 (.8)

$100 \leq n, m \leq 10^{5}$.

## Input

The first line of input contains two integers, $n$ and $m$.
Following are $m$ lines $i$-th of which contains two integers $l_{i}$ and $r_{i}$.

## Output

Output the answer.

## Examples

### Input 

```
5 2
1 2
4 5
```

### Output

```
1
```

### Explanation

Time slots $1$ and $2$ are booked by the first person. Time slots $4$ and $5$ are booked by the second person. The only remaining vacant time slot is the time slot $3$, so the answer is $1$.

### Input

```
6 3
1 4
2 5
6 6
```

### Output
```
0
```

### Explanation

Time slots $1$, $2$, $3$, and $4$ are booked by the first person. Time slot $5$ is booked by the second person. Time slot $6$ is booked by the third person. Because there's no single time slot available for pianists, the answer is $0$.