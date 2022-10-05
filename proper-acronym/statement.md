# Proper Acronym

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

Kay is struggling with memorising the medical terms he learnt at his clinical workshop. Now he has to remember the term that consists of $n$ words. To facilitate memorisation, Kay generated an acronym of the term, which is given as $s$. Check if $s$ is really a proper acronym of the term.

Note that, acronym is an abbreviation formed from the initial letters of other words and pronounced as a word. 

## Constraints

$1 \leq n \leq 10$. The length of each word in the medical term never exceeds $10$. 
It is guaranteed that the initial letter of each word is capitalised.

## Input

The first line of input contains an integer, $n$.
The second line of input contains $n$ words which compose a name of the medical term.
The third line of input conatins a though-to-be proper acronym, $s$.

## Output

If $s$ is a proper acronym, output "Yes". Otherwise, output "No".

## Examples

### Input

```
3
Acute Mountain Sickness
AMS
```

### Output

```
Yes
```

### Explanation

The acronym for Acute Mountain Sickness is AMS. Kay also gave AMS as $s$. It is clearly correct.

### Input

```
3
Computerised Axial Tomography
DOG
```

### Output
```
No
```

### Explanation

The acronym for Computerised Axial Tomography is CAT. However Kay gave DOG. It is incorrect.