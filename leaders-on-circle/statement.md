# Leaders on Circle

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

Today the World GX summit is held in London. In this summit, $X$ political leaders from each of $X$ countries are invited and discuss the global issues. You, belonging to the department that is in charge of hosting a conference, are asked to arrange the first conference room today. However, you noticed that there're only $Y$ chairs available around a circular table. 

Having reported this matter to your boss, she tells you to pick up $Y$ leaders from $X$ of them, and after you assign seats to everyone, rotate the entire table such that the country with name of the lowest alphabetical (lexicographic) order is facing directly north.

While trying to achieve your task, you wonder how many possible ways there are to pick up $Y$ leaders from $X$ of them and arrange them around a circular table that satisfy your boss's command.

Since the answer can be astronomically large, your task is to find out the answer modulo $10^{9} + 7$. In other word, output the remainder of the answer divided by $10^{9} + 7$.

## Constraints

$1 \leq Y \leq X \leq 10^{6}$.

## Input

The input contains two integers in a single line: $X$ and $Y$.

## Output

Output the answer modulo $10^{9} + 7$.

## Examples

### Input

```
5 3
```

### Output

```
20
```

### Explanation

First of all, there're $10$ ways to pick up $3$ leaders from $5$ participating leaders. Then, once $3$ leaders can be allocated to each table, of which there're $2$ ways to do so. Thus, the answer is $10 × 2 = 20$ ways.

### Input

```
294 72
```

### Output

```
524723643
```