# Friend and Friend of Friend

## Author

Kay Akashi

## Time (ms)

1000

## Memory (kb)

256000

## Difficulty

☆☆☆

## Tags

## Problem Statement 

On the social media platform Imstagran, you are assigned an index $x$ $(1 \leq x \leq n)$. You are going to be a friend with a certain number of people amongst $(n - 1)$ people each of which is assigned an index ranging from $1$ to $n$ but not $x$ ($i.e.$ People including you are assigned distinct indices from $1$ to $n$).

In $m$ lines you are given $a_i$ and $b_i$ $(1 \leq i \leq m)$ indicating that $a_i$ and $b_i$ are friends on Imstagran. Now, you are asked to count the number of people who are either "your friends" or "friends of your friends". Clearly, you yourself are "a friend of your friend" hence counted, only if you have any friend. If you are "lonely enough" ($i.e.$ you don't have a single friend), you are NOT "a friend of your friend" hence not counted, sadly.

Note that, unlike Imstagran's rival social media Instagram, it never happens that one follows another but not followed back. On Imstagran, two people are friends and they bilaterally follow each other. 

## Constraints

$2 \leq n, m \leq 10^{4}$,
$1 \leq a_i, b_i \leq n$ $(1 \leq i \leq m)$.


## Input

The first line of input contains three integers, $n$,  $x$, and $m$.
Following are $m$ lines each of which consists of $a_i, b_i$ $(1 \leq a_i, b_i \leq n)$, $(1 \leq i \leq m)$.


## Output

Output the answer.

## Examples

### Input

```
4 2 3
1 4
2 4
2 3
```

### Output

```
4
```

### Explanation

You can see that $3$ and $4$ are your friends. You, whose index is $2$, are a friend of $1$ and $2$. Also, $1$ is a friend of your friend $4$, hence a friend of your friend. All people here meet the condition, thus the answer is $4$.

### Input

```
5 1 2
3 4
4 5
```

### Output
```
0
```


### Explanation

You have no friend. Because you have no friend, there're no friends of your friend. The answer is $0$.
