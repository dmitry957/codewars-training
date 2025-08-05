# How many socks for a pair?

[Codewars Link](https://www.codewars.com/kata/6863033d9c452af74e0983b7/python)

## Description

I have a number of different colours of socks mixed up in a drawer and I require a number of matching pairs of socks. Fortunately, I don't mind what colour the pairs are and I have an infinite number of each colour of sock.

Your task is to create a function with inputs `colours` and `pairs` that returns the minimum number of socks that I would have to take from my drawer to guarantee `pairs` number of matching pairs.

### Example

`socks(2, 1)` should equal `3` because it takes 3 socks to guarantee a pair of socks with 2 different possible colours to select from.

### More examples

```
socks(1, 2) = 4
socks(2, 3) = 7
socks(4, 2) = 7
socks(4, 4) = 11
```

> Note: `colours` and `pairs` are both positive integers.

#Fundamentals #Mathematics