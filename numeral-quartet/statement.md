# Numeral Quartet

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

You are given four distinct numbers $A$, $B$, $C$, and $D$ ($1 \leq A, B, C, D \leq 9$). Given an integer $K$, output all the values smaller than $10^{K}$ each digit of which is either $A$, $B$, $C$, or $D$, in an increasing order in a single line.

## Constraints

$1 \leq K \leq 9$.

### Subtask 1 (.2)

$1 \leq K \lt 5$.

### Subtask 2 (.8)

$5 \leq K \leq 9$.

## Input

The first line contains one number, $K$.
The second line contains four numbers, $A$, $B$, $C$, and $D$.

## Output

Output the values in a single line, with values separated by a single space.

## Examples

### Input 

```
1
3 7 2 4
```

### Output

```
2 3 4 7
```

### Input

```
3
1 2 3 4
```

### Output
```
1 2 3 4 11 12 13 14 21 22 23 24 31 32 33 34 41 42 43 44 111 112 113 114 121 122 123 124 131 132 133 134 141 142 143 144 211 212 213 214 221 222 223 224 231 232 233 234 241 242 243 244 311 312 313 314 321 322 323 324 331 332 333 334 341 342 343 344 411 412 413 414 421 422 423 424 431 432 433 434 441 442 443 444
```