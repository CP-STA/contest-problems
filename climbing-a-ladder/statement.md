# Climbing a Ladder

## Author

Deyao Chen

## Time (ms)

1000

## Memory (kb)

256000

## Difficulty 

☆☆☆☆☆

## Tags

maths, dynamic programming

## Problem Statement
You are designing an open world game. In the game, a character can climb a ladder to move up. In each move, the character can either climb up one unit by pressing the up arrow, or leap up 3 moves by pressing x. Note that if there is less than 3 units left of the ladder, the player can still choose to leap.

Now you want the game to drop a loot whenever the player does a specific combination of moves and leaps. (Think of this as a sort of hidden cheat code or hidden combo) Obviously, the higher the ladder, the more unlikely the player will randomly stumble across the specific combination. So you decide to count the number of combinations of moves given the height of a ladder to gauge the difficulty of achieving the hidden combo.

For example, if the ladder is 5 units high, the number of combinations of moves is 9:

- climb x5
- climb x4, leap
- climb x3, leap 
- climb x2, leap
- climb, leap, climb
- climb, leap, leap
- leap, climb, climb
- leap, climb, leap
- leap, leap

## Constraints

$1 \le n \le 10^{15}$

### Subtask 1 (.2)

$1 \le n \le 20$

### Subtask 2 (.2)

$1 \le n \le 10^{3}$

### Subtask 3 (.2)

$1 \le n \le 10^{5}$

### Subtask 4 (.4)

No more constraints.

## Input

Input one number, $n$, the height of the ladder

## Output

Output one number, $a$, the remainder of the number of combinations of moves divided by 10^9+7.

## Examples

### Input

```
5
```

### Output

```
9
```
