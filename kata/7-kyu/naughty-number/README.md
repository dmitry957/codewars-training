# Naughty number

[Codewars Kata Link](https://www.codewars.com/kata/679bdbe30a5faf7bbf634e0f/python)

## Description

There is a naughty number hidden somewhere in the list. Find the index of it, if you are strong enough, of course!

### Input:
You will receive an array of arrays (a list of lists).
Each sub-array can only contain either another array or a single number.
There will always be at least one sub-array in the input.
There will be only one number hidden in the sub-arrays

### Output:
Return the index of the first-level sub-array that contains the hidden number.

### Examples:

```python
[ [[[]]] , [[]], [], [], [[2]] ] -> index is 4
[ [1] ] -> index is 0
[ [], [8], [] , [] ] -> index is 1
```

---

#Lists #Arrays