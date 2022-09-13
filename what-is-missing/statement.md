# What is Missing

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

Given two strings $s$ and $t$, report what letters should $t$ be supplemented with so that $t$ can be identical to $s$ by arranging the letters in $t$ appropriately.

Note that, both $s$ and $t$ consist of only small Latin letters.

It is guaranteed that the answer exists.

In the first example, if you re-arrange $t$ and makes it "chch" and compares it with $s$, "church", you can notice that $1$ "u" and $1$ "r" are missing. Because "r" is lexicographically smaller than "u", the answer should be in the order shown in the example output.

In the second example, you don't need to re-arrange $t$, but all vowels are missing: $1$ "o", $3$ "i"s, and $2$ "a"s. 

## Constraints

Lengths of $s$ and $t$ never exceed $10^{6}$.

## Input

The first line of input contains a string $s$.
The second line of input contains a string $t$.

## Output

In each line, output the missing letter and its number, separated by a single space.
Letters should be in lexicographically increasing order.

## Examples

### Input

```
church
cchh
```

### Output

```
r 1
u 1
```

### Input

```
koichiakashi
kchksh
```

### Output
```
a 2
i 3
o 1
```