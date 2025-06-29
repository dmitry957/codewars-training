# Compound Array

**Kata Link:** [https://www.codewars.com/kata/56044de2aa75e28875000017/python](https://www.codewars.com/kata/56044de2aa75e28875000017/python)

## Problem Description

You have to create a method `compoundArray` which should take as input two int arrays of different length and return one int array with numbers of both arrays shuffled one by one.

## Task

Create a function that:
- Takes two integer arrays of different lengths as input
- Returns a single integer array with elements from both arrays interleaved
- Shuffles the elements one by one from each array

## Example

**Input:** 
- Array 1: `{1, 2, 3, 4, 5, 6}`
- Array 2: `{9, 8, 7, 6}`

**Output:** `{1, 9, 2, 8, 3, 7, 4, 6, 5, 6}`

### How it works:
1. Take first element from Array 1: `1`
2. Take first element from Array 2: `9`
3. Take second element from Array 1: `2`
4. Take second element from Array 2: `8`
5. Continue alternating until all elements are used

## Tags

`#Arrays` `#Fundamentals`