# Large Shift Caesar Cipher

## Author

Kay Akashi

## Time (ms)

1000

## Memory (kb)

256000

## Difficulty

☆☆☆

## Tags

## Problem Statement 

You are given a key $k$ and a string $s$ consisting of $n$ small Latin letters. Your task is to perform the following operation on each letter in $s$:

you change it to the letter which is $k$ letters ahead of the original letter. For example, if $k = 2$ and the letter is "b", you change "b" to "d". In case you come to "z" and still have to move the letters, go back to "a". For example, if $k = 4$ and the letter is "y", this is changed to "c". 

Note that, if $k$ is negative, you change the letter to $k$ letters behind the original letter.

## Constraints

$1 \leq n \leq 10^{5}$, $-10^{4} \leq k \leq 10^{4}$. $s$ consists of only small Latin letters.

## Input

The first line of input contains two integers, $n$ and $k$.
The second line of input contains one string, $s$.

## Output

Output the resulting string.

## Examples

### Input

```
12 3
cryptography
```

### Output

```
fubswrjudskb
```

### Input

```
9 -1281
standrews
```

### Output
```
lmtgwkxpl
```