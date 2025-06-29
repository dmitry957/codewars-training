# Alternate Square Sum

**Kata Link:** [https://www.codewars.com/kata/559d7951ce5e0da654000073/python](https://www.codewars.com/kata/559d7951ce5e0da654000073/python)

## Problem Description

Complete the function that takes an array of integers as input and finds the sum of squares of the elements at even positions (i.e. 2nd, 4th, etc.) plus the sum of the rest of the elements at odd positions.

## Task

Create a function that:
- Takes an array of integers as input
- Squares the elements at even positions (2nd, 4th, 6th, etc.)
- Keeps the elements at odd positions as they are
- Returns the sum of all these values

## Important Notes

- For empty arrays, the result should be zero (except for Haskell)
- The values at even positions need to be squared
- For languages with zero-based indices, this will occur at oddly-indexed locations
- In Python, the values at indices 1, 3, 5, etc. should be squared because these are the second, fourth, and sixth positions in the list

## Example

**Input:** `[11, 12, 13, 14, 15]`  
**Output:** `379`

### Position Mapping:
```
Index:  0   1   2   3   4
Value: 11  12  13  14  15
Pos:    1   2   3   4   5
```

### Calculation:
- Elements at odd positions (indices 0, 2, 4): `11 + 13 + 15 = 39`
- Elements at even positions (indices 1, 3): `12² + 14² = 144 + 196 = 340`
- **Total:** `39 + 340 = 379`

### Explanation:
- Elements at indices 0, 2, 4 are 11, 13, 15 and they are at odd positions (positions #1, #3, #5)
- Elements at indices 1, 3 are 12 and 14 and they are at even positions (positions #2, #4)
- We add 11, 13, 15 as they are and square 12 and 14

## Tags

`#Fundamentals` `#Arrays` `#Lists`