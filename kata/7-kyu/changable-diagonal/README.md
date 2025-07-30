# Changable Diagonal

[Codewars Kata Link](https://www.codewars.com/kata/68508d8937ee53321e405d31/python)

## Description

### Task

Given a matrix (NxN) and a specific value.

#### Input:

```python
matrix = [[ 1,  2,  3,  4],
          [ 5,  6,  7,  8],
          [ 9, 10, 11, 12],
          [13, 14, 15, 16]]
 
value = 2
```

What this value does is it changes the main diagonal of the matrix. The main diagonal is basically the trace of the matrix (read this article, in case you are unaware of what the trace is). If value > 0, then the main diagonal drops down, if value < 0, the main diagonal goes up and if value = 0, the diagonal does not change. With this example here (I marked the diagonal numbers with *):

```
[[*1,   2,   3,   4],
 [ 5,  *6,   7,   8],
 [ 9,  10, *11,  12],
 [13,  14,  15, *16]]
 
The main diagonal here is [1, 6, 11, 16] but with given value:

[[ 1,   2,  3,  4],
 [ 5,   6,  7,  8],
 [*9,  10, 11, 12],
 [13, *14, 15, 16]]
 
The main diagonal is [9, 14].

In case of the value being negative, for example -2:

[[ 1,  2, *3,  4],
 [ 5,  6,  7, *8],
 [ 9, 10, 11, 12],
 [13, 14, 15, 16]]
 
The main diagonal is [3, 8].
With these rules being said, find the sum of the trace of a matrix with the given value. The value will never exceed or reach the length of an array.

#Matrix #Algorithms