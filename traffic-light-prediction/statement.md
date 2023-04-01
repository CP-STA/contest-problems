# Traffic Light Prediction

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

The colour of traffic light in the town of Leveen changes periodically in a following fashion: green → yellow → red → yellow → green → yellow → red → yellow → green → .... The colour turns green at 00:00:00 of each day, and we know that green light lasts for $g$ seconds, yellow light lasts for $y$ seconds, and red light lasts for $r$ seconds. 

Now, $t$ seconds have passed since 00:00:00. Your task is to tell which colour is shown in the traffic light at the time of $t$.

If $t$ is exactly the time when the light turns one from another, output the colour AFTER the change.

Note that, no matter what colour is shown at 23:59:59 in the previous day, the colour turns green at 00:00:00.

## Constraints

$1 \leq g, y, r \leq 100$, $0 \leq t \leq 86400$.

## Input

The first line of input contains three integers, $g$, $y$, $r$.
The second line of input contains one integer, $t$.

## Output

Answer the colour from three choices: "green", "yellow", "red".

## Examples

### Input

```
10 2 10
70
```

### Output

```
yellow
```

### Explanation

- 00:00:00 → the light turns green.
- 00:00:10 → the light turns yellow.
- 00:00:12 → the light turns red.
- 00:00:22 → the light turns yellow.
- 00:00:24 → the light turns green.
- 00:00:34 → the light turns yellow. 
- 00:00:36 → the light turns red.
- 00:00:46 → the light turns yellow.
- 00:00:48 → the light turns green.
- 00:00:58 → the light turns yellow.
- 00:01:00 → the light turns red.
- 00:01:10 → the light turns yellow.

At the time of $t = 70$, the light turns yellow from red. Hence the answer is yellow.

### Input

```
48 12 41
0
```

### Output

```
green
```

### Explanation

Regardless of the colour shown in the last minute of previous day, at $t = 0$ the colour turns green in the very beginning of the day.