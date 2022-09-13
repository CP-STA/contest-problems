# Taxi Fare

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

In Tokyo, initial taxi fare is $X$ yen. Taxi fare increases by every kilometer by $Y$ yen. 
One day, Kay has moved $Z$ meters by taxi. How much should he pay for the fare?

In the first example, taxi fare starts at $410$ yen. The fare increases by $400$ yen at the point where Kay has moved $1000$m (= $1$km). Hence the total fare is $810$ yen.

In the second example, taxi fare starts at $0$ yen. Because Kay travelled by less than a kilometer, the fare never increases. Hence the total fare is $0$ yen.

## Constraints

$0 \leq X \leq 1000$, $0 \leq Y \leq 500$, $0 \leq Z \leq 10000$.

## Input

The input contains three integers in a single line: $X$, $Y$, and $Z$.

## Output

Output the taxi fare in yen.

## Examples

### Input

```
410 400 1900
```

### Output

```
810
```

### Input

```
0 100 944
```

### Output
```
0
```