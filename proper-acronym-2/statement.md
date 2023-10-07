# Proper Acronym 2

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

(This problem is a continuation of [Proper Acronym](https://judge.cpsta.co.uk/problems/proper-acronym). )

Kay is still struggling with memorising the medical terms today. Recently, Kay is observing weird acronyms that are in common use in the field of medicine. For example, in his oncology lecture, he learnt the protein named Human Epidermal Growth Factor Receptor 2 (the protein that promotes the growth of cancer cells particularly in female breast). Seeing this protein name, he initially presumed that the given acronym for this protein was "HEGFR2". However, the acronym widely acknowledged for this is actually "HER2"! 

The rule for this sort of acronym is that, you can take the first letters of each word that composes the name, but don't necessarily have to take all of them unless the resulting acronym becomes an empty sequence. Also, the order of letters must not be altered. Furthermore, you must not include any letter that does not appear in the original name. Lastly, you are not allowed to duplicate the letters. (e.g. Technically, Human Epidermal Growth Factor Receptor 2 can be HER2, HGF, E, or R2, but cannot be RH2, HER3, HHEEGGFFRR22, or 2RFGEH (not exhaustive)). 

Based on the aforementioned rules, your task is to judge if the given acronym $T$ is validly working as a proper acronym of the medical term $S$ consisting of $N$ words also given in the input.

## Constraints

$1 \leq |T| \leq N \leq 5000$. Length of word in $S$ never exceeds $10$.

### Subtask 1 (.2)

$1 \leq |T| \leq N \leq 10$.

### Subtask 2 (.8)

$1 \leq |T| \leq N \leq 5000$.

## Input

The first line of input consists of single integer, $N$, the number of words that compose $S$.
The second line of input contains $N$ words, forming $S$.
The third line of input contains one string, $T$, an acronym whose validity you have to judge.

It is ensured that the first letter of each word composing $S$ is either a capital Latin letter or an Arabic numeral. 

## Output

If $T$ is a proper acronym of $S$, output "Yes". Otherwise, "No".

## Examples

### Input 

```
6
Human Epidermal Growth Factor Receptor 2
HER2
```

### Output

```
Yes
```

### Input

```
3
Patent Foramen Ovale
PFO
```

### Output
```
Yes
```

### Input

```
4
Coronary Artery Bypass Graft
CBAG
```

### Output
```
No
```

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

### Input

```
3
Volume Of Distribution
DV
```

### Output
```
No
```
