# Protein Master

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

You are reading a book "vegetal protein encyclopaedia" which contains myriads of information about vegetables and their protein quantities (g) contained in $100$kg of each of them. While reading from the top to bottom, you take notes of vegetables of your interest and their protein quantities on a piece of paper. During your work, Kay intermittently interrupts and asks you "Can you tell me the name of the vegetable which is second least abundant in protein on your note?". Hence your task is to report a name of the vegetable which is second least abundant in protein amongst vegetables you have written down on your paper so far. Be noted that the protein quantities of vegetables are all distinct.

In the first example, the nutrition order transfers in a following way (the least nutritious vegetable comes in the left and the most nutritious vegetable comes in the right): [mashroom] → [tomato, mashroom] → [tomato, potato, mashroom] → (OUT: potato) → [tomato, cucumber, potato, mashroom] → (OUT: cucumber) → (OUT: cucumber).

In the second example, the nutrition order transfers in a following way: [pumpkin] → [pumpkin, okra] → [leet, pumpkin, okra] → (OUT: pumpkin) → [leet, pumpkin, okra, barley] → (OUT: pumpkin).

## Constraints

$3 \leq q \leq 10^{4}$. 

### Subtask 1 (.2)

$3 \leq q \lt 100$.

### Subtask 2 (.8)

$100 \leq q \leq 10^{4}$.

## Input

The first line contains one integer $q$, the number of queries you are to process.
Following are $q$ lines each of which is classified as either of two types of queries:
$1$- if the first element of an input is "IN", vegetable name and its protein quantity follow, all separated by single spaces (e.g. IN tomato $7$).
$2$- if the first element of an input is "OUT", report the vegetable name which is second least abundant in protein amongst those written down on your note so far.
It is guaranteed that all protein quantities are whole numbers and all distinct, and you are not asked to report a vegetable name until three or more vegetables are on your note.


## Output

Output the second-least-protein-abundant vegetable name in each line.

## Examples

### Input 

```
9
IN mashroom 2910
IN tomato 700
IN potato 2201
OUT
IN cucumber 999
OUT
IN barley 6103
OUT
OUT
```

### Output

```
potato
cucumber
cucumber 
cucumber
```

### Input

```
6
IN pumpkin 1119
IN okra 2114
IN leet 522
OUT
IN barley 6103
OUT
```

### Output
```
pumpkin
pumpkin
```