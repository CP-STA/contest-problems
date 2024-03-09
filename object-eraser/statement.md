# Object Eraser

## Author

Kay Akashi

## Time (ms)

2000

## Memory (kb)

256000

## Difficulty

☆☆☆

## Tags

## Problem Statement 

Japanese alphabets are often more complex than those of English, thus each of them has multiple "strokes". For example, "depression" in Japanese is "鬱" that requires $29$ strokes. 

Kay has written a sentence in Japanese on his tablet. Now, Kay knows his sentence consists of $N$ characters, and $i$-th character has $A_i$ characters. 

His tablet has a function called "object eraser" which enables him to delete the last stroke from the last character. After deleting all the strokes in a single character, the character is completely erased.

He says he is going to press the object eraser button $K$ times, but is unsure how many characters are going to be completely erased. Tell him the answer.

## Constraints

$1 \leq N \leq 10^{5}$.
$0 \leq K \leq 10^{12}$.
$1 \leq A_i \leq 10^{9}$ ($1 \leq i \leq N$).

Apologies for unrealistic constraints (no Japanese character requires as many as $1$ billion strokes in reality).

## Input

The first line of input contains two integers, $N$ and $K$.
The second line of input contains $N$ integers, $A_1, A_2, ..., A_N$.

## Output

Output a single integer, the number of characters being erased completely.

## Examples

### Input

```
5 6
3 2 5 2 2
```

### Output

```
2
```

### Explanation

The sentence is "ありがとう" (*arigatou*, meaning "thank you"). After pressing the button $6$ times, the last two characters are completely gone, but the third letter remains undeleted, only to transfer "が" to "か".


### Input

```
2 12
7 5
```

### Output
```
2
```

### Explanation

"寿司" (*sushi*, meaning "sushi"). Every character is gone after pressing the button $12$ times because the word as a whole consists of $12$ strokes. 

### Input

```
29 40
12 9 3 3 3 2 2 3 1 2 3 15 14 1 1 1 2 1 3 2 5 2 2 4 5 2 3 2 1
```

### Output
```
16
```
### Explanation

"最後までテストケースを確認してくれてありがとうございます。" (well, just use a translator if you're interested). 
