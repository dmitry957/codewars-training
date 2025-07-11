# Simple Fun #61: Crossing Sum

[Codewars Kata Link](https://www.codewars.com/kata/5889ab4928c08c08da00009b/python)

## Description
### Task
Given a rectangular matrix and integers a and b, consider the union of the ath row and the bth (both 0-based) column of the matrix. Return sum of all elements of that union.

### Example
For
```
matrix = [[1, 1, 1, 1],
          [2, 2, 2, 2],
          [3, 3, 3, 3]]
a = 1
b = 3
```
the output should be 12.

Here `(2 + 2 + 2 + 2) + (1 + 3) = 12`.

### Input/Output
- **[input] 2D integer array** `matrix`
  - 2-dimensional array of integers representing a rectangular matrix.
  - Constraints: 1 ≤ matrix.length ≤ 5, 1 ≤ matrix[0].length ≤ 5, 1 ≤ matrix[i][j] ≤ 100.
- **[input] integer** `a`
  - A non-negative integer less than the number of matrix rows.
  - Constraints: 0 ≤ a < matrix.length.
- **[input] integer** `b`
  - A non-negative integer less than the number of matrix columns.
  - Constraints: 0 ≤ b < matrix[i].length.
- **[output] an integer**

#Puzzles