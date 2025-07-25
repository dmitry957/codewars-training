# Construct a bit vector set

<https://www.codewars.com/kata/52f5424d0531259cfc000d04/python>

## Description

### Task
Write a function which accepts a sequence of unique integers ( 0 <= x < 32 ) as an argument and returns a 32-bit integer such that the integer, in its binary representation, has 1 at only those indices, numbered from right to left, which are in the sequence.

### Examples

```python
[0, 1]  ->  3
[1, 2, 0, 4]  ->   23
```

Because 23 in binary is

```
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 1 1
                                      . . . . . 5 4 3 2 1 0  <-  indices
                                                  ^   ^ ^ ^
                                                  these bits are 1
      due to the corresponding indices being in the given sequence
```

---
*Algorithms*
