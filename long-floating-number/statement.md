# Long Floating Number

## Author

Kay Akashi

## Time (ms)

2000

## Memory (kb)

256000

## Difficulty

☆☆

## Tags

## Problem Statement 

Given a positive decimal $N$, judge whether $N$ is smaller than, equal to, or larger than $1$.

Note that, $N$ may contain trailing zeros (e.g. $N = 1.4040000000$).
 
## Constraints

$0 \leq N \lt 2$.

## Input

The first line of input is a single floating value, $N$.
$N$ is given with as many as $1000$ decimal places.

## Output

If $N \lt 1$, output "smaller". If $N = 1$, output "equal". If $1 \lt N$, output "larger".

## Examples

### Input

```
1.925
```

### Output

```
larger
```


### Input

```
0.000000000000000000003
```

### Output
```
smaller
```

### Input

```
1.00000
```

### Output
```
equal
```
