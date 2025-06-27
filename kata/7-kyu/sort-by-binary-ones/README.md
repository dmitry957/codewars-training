# Sort by Binary Ones

[Codewars Kata Link](https://www.codewars.com/kata/59eb28fb0a2bffafbb0000d6/python)

In this kata, you need to implement a function that sorts a list of integers based on their binary representation.

The rules are simple:

1. Sort the list based on the amount of 1's in the binary representation of each number.
2. If two numbers have the same amount of 1's, the shorter binary string goes first. (e.g., `"11"` goes before `"101"` when sorting 3 and 5 respectively)
3. If the binary strings have the same length, the lower decimal number goes first. (e.g., 21 = `"10101"` and 25 = `"11001"`, then 21 goes first as it is lower)

## Examples

Input:

```python
[1, 15, 5, 7, 3]
```

In binary strings: `["1", "1111", "101", "111", "11"]`

Output:

```python
[15, 7, 3, 5, 1]
```

After `sortByBinaryOnes`: `["1111", "111", "11", "101", "1"]`

---

#Arrays #Lists #Algorithms #Sorting #Binary #Bits