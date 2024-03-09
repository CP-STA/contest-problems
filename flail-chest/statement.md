# Flail Chest

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

Human body has $12$ pairs of ribs. Rib cage forms the chest cavity, and protects important organs inside. 

Because of fragility, ribs are prone to fracture by trauma. Flail chest is a medical term that describes the specific rib fracture pattern, and is defined as follows: the rib fractures where $3$ or more adjacent ribs are broken.

You will receive a string $S$ of length $12$ each letter of which is either "o" (intact) or "x" (fractured) that you collected from your patient. $i$-th letter states the status of $i$-th rib $(1 \leq i \leq 12)$. Your task is to judge whether their fracture pattern is categorised as flail chest or not.

## Constraints

Each letter in $S$ is either "o" or "x".

## Input

The input consists of a single string, $S$.

## Output

If $S$ signifies flail chest, output "Yes" (case-specific). Otherwise, output "No".

## Examples

### Input 

```
oxxxoooooooo
```

### Output

```
Yes
```

### Explanation

The $2$nd, $3$rd, and $4$th ribs are broken. Because there're $3$ consecutive affected ribs, it's categorised as flail chest.

### Input

```
oxxoxxoxxoxx
```

### Output
```
No
```

### Explanation

Despite the tragedy, no $3$ adjacent ribs underwent fracture. This is not flail chest.

### Input 

```
oooooooooooo
```

### Output

```
No
```

### Explanation

Why the heck did this patient come to see a doctor?

### Input 

```
xxxxoxxoxxxx
```

### Output

```
Yes
```

### Explanation

Note that there may be several triplets of broken ribs. 