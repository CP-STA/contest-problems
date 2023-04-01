# Rondon Underground

## Author

Deyao Chen

## Time (ms)

1000

## Memory (kb)

256000

## Difficulty

☆☆☆☆

## Tags

## Problem Statement

You and your friend Kay are taking the underground train / tube system to travel around the city Rondon. The doors are close as you approach the train at station $p$. Kay barely squeezes through the small gap of the closing doors whereas you are left behind. You signal with hand gesture that he should return to the same station to meet you so you can travel together later. To kill some time, you find a seat on the platform, take out your phone and start watching a movie. After $k$ minutes, you put your phone down but Kay is nowhere to be seen on the train that has just arrived. To get an idea of whereabouts of Kay, you decide to count the number of routes to get back to station $p$ that takes him exactly $k$ minutes, and the total number of routes possible in exactly $k$ minutes. 

All trains in the system run in both direction. It is possible for two lines to run parallel for a few stations. For example, line $A$ might go from station $1$ - $2$  - $3$ - $4$ while train $B$ might run from station $5$ - $2$ - $3$ - $6$. Taking different lines counts as a different route even if the stations you go through are the same. It takes $1$ minute to get to one station from adjacent stations. Changing trains takes no time; Kay is on a train all the time, spending no time on the platform. Kay might have returned to station $p$ while you were watching a movie but there's no way you could have seen him.

It is guaranteed that the sum of the number of stations $n$ across all the lines never exceededs $15$. All the stations are numbered sequentially from $1$ to $m$, the number of stations that at least one train passes through. For example, if line $A$ goes through $1$ - $2$ - $3$ and line $B$ goes through $2$ - $3$ - $4$, $n = 6$ and $m = 4$ (note that in this case station $5$ and $6$ are connected to nowhere else). The number of lines is denoted as $q$. It is also guaranteed that each line connects at least two stations.

## Constraints

$1 \le k \le 10^{18}$
$2 \le n \le 15$

### Subtask 1 (.1)
There is only one train line. 

### Subtask 2 (.2)
$1 \le k \le 7$ and $2 \le n \le 10$
There is no pair of two lines running in parallel.

### Subtask 3 (.1)
$1 \le k \le 7$ and $2 \le n \le 10$

### Subtask 4 (.4)
There is no pair of two lines running in parallel.

### Subtask 5 (.2)
No more constraints

## Input

The first line contains four numbers, $k$, $m$, $p$, and $q$ which is the number of minute you wait, the number of stations, the station you are currently on, and the number of lines. 

In the next $q$ lines, each line denotes the stations a train line goes through. These stations are numbered from 1 to m. 

## Output

Output two numbers -- the number of routes get back to the same station in $k$ minute and the number of total possible routes in $k$ minutes. Since the numbers can be really large, output the remainder of the answers divided by $10^9 + 7$. 

## Examples

### Input

```
2 10 6 1
1 6 8
```

### Output

```
2 2
```

### Explanation

In this example, there is a line running from station 1 - 6 - 8, with a total of 10 stations in the system (some stations might be connected to nowhere). You wait in station 6 for 2 minutes, there are two ways Kay could have gone: 6 - 1 - 6 or 6 - 8 - 6. There are also only two total ways. 

### Input

```
2 10 6 2
1 6 8
1 6 8
```

### Output

```
8 8
```

### Explanation

There are two lines running from station 1 - 6 - 8. There are 8 ways Kay could have gone. Let's say kay went through station 6 - 1 - 6, he can take line 1 then line 1, line 1 then line 2, line 2 then line 1, or line 2 then line 2. There are 4 paths in this scenario. The same goes for the other way, making a total of 8 ways. 

### Input 

```
4 3 2 3
1 3
1 3
2 1
```

### Output

```
5 15
```

