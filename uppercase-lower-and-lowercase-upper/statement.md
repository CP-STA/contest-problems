# Uppercase Lower and Lowercase Upper

## Author

Kay Akashi

## Time (ms)

1000

## Memory (kb)

256000

## Difficulty

☆☆

## Tags

## Problem Statement 

Given an integer $n$ and string $s$ of length $n$, Kay asks you to convert $s$ into $t$ in such a way that $t[i]$ is an uppercase letter of $s[i]$ in case $s[i]$ is a lowercase letter, and $t[i]$ is a lowercase letter of $s[i]$ in case $s[i]$ is an uppercase letter $(1 \leq i \leq n)$. It is guaranteed that any $s[i]$ is either a lowercase or uppercase Latin alphabet $(1 \leq i \leq n)$.

## Constraints

$1 \leq n \leq 10^{5}$.

## Input

The first line of input contains an integer $n$, the length of $s$.
The second line contains a string $s$.

## Output

Output the resulting string.

## Examples

### Input

```
20
UniversityOfStAndrews
```

### Output

```
uNIVERSITYoFsTaNDREWS
```

### Input

```
11
goodmorning
```

### Output
```
GOODMORNING
```