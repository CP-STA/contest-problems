# Earliest Date

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

In $n$ lines, you are given dates in yyyy/mm/dd format. Output the earliest date amongst those.

## Constraints

$1 \leq n \leq 10^{5}$.

## Input

The first line of input contains one integer, $n$.
Following are $n$ lines each of which contains a date in yyyy/mm/dd format.

## Output

Output the answer.

## Examples

### Input

```
3
2010/05/11
1979/05/04
2019/07/04
```

### Output

```
1979/05/04
```

### Explanation

The earliest date amongst 3 dates when David Cameron (2010/05/11), Margaret Thatcher (1979/05/04), and Boris Johnson (2019/07/04) became a Prime Minister in the British Parliament, is clearly $1979/05/04$ of Margaret Thatcher.

### Input

```
2
1413/08/28
1413/08/28
```

### Output
```
1413/08/28
```

### Explanation

The testcase can contain duplicate dates, in this case, date of establishment of the University of St Andrews. In this case, output any.
