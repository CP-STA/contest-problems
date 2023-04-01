# Local Anaesthetics

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

Local anaesthetics are a collection of anaesthetics that are administered where loss of consciousness is neither desired nor necessary. They are helpful in avoiding high-dose of general anaesthetics, and even as a post-operative analgesia to relieve a pain.

One way to classify local anaesthetics is to look at the "onset" and "duration". Onset means how fast the anaesthetic starts to show its effect, and is either "rapid", "medium", or "slow". Duration means how long the anaesthetic effect lasts, and is either "long", "medium", or "short". In each of $N$ lines, you are given the name of anaesthetic, onset, and duration.

Then in each of $M$ lines, you are given a desired onset and duration. Your task is, for each query, to output all the names of drugs that have desired onset and duration, in a lexicographically ascending order. Note that, each answer should be shown in a single line, with drug names separated by a comma and a space. If there's no such drug, output "NONE" instead.

Also note that, anaesthetic name consists of only small Latin alphabets.

## Constraints

$1 \leq N, M \leq 1000$. The length of drug name never exceeds $20$.

## Input

In the first line, you are given $N$, the number of drugs whose information you receive to create a "formulary".
In following $N$ lines, you are given an anaesthetic name, onset, and duration separated by a space in between.
In $(N + 2)$-th line, you are given $M$, the number of queries.
In following $M$ lines, you are given a desired onset and duration separate by a space in between.

## Output

In $M$ lines, for each query, you output the drug names that satisfy the conditions of onset and duration that you were given, in a lexicographically increasing order, with comma and a space in between.

## Examples

### Input

```
4
lidocaine rapid medium
tetracaine slow long
bupivacaine slow long
articaine rapid short
3
rapid short
medium medium
slow long
```

### Output

```
articaine
NONE
bupivacaine, tetracaine
```

### Explanation

In the first query, you are asked to output the names of drugs that have rapid onset and short duration. When you have a look at the given formulary, you can see that it is only articaine that satisfies the condition. Thus, you just output "articaine".

In the second query, you need to find anaesthetics that have medium onset and medium duration. However, because there's no such a drug, you output "NONE" so that it is clear that you did not find any drug suitable.

In the third query, we have tetracaine and bupivacaine as anaesthetics that have slow onset and long duration. However, be noted that you should output those names in lexicographically ascending order, that is, bupivacaine and tetracaine, rather than tetracaine and bupivacaine. Also note that they are all shown in a single line separated by a comma and a space (no comma at rightmost and leftmost end!).
