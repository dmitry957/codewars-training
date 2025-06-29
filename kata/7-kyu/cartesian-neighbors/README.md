# Cartesian Neighbors

**Kata Link:** [https://www.codewars.com/kata/58989a079c70093f3e00008d/python](https://www.codewars.com/kata/58989a079c70093f3e00008d/python)

## Problem Description

A Cartesian coordinate system is a coordinate system that specifies each point uniquely in a plane by a pair of numerical coordinates, which are the signed distances to the point from two fixed perpendicular directed lines, measured in the same unit of length.

The coordinates of a point in the grid are written as `(x,y)`. Each point in a coordinate system has eight neighboring points, provided that the grid step = 1.

## Task

Write a function that takes a coordinate on the x-axis and y-axis and returns a list of all the neighboring points. Points inside your returned list need not be sorted (any order is valid).

## Examples

### Example 1
**Input:** `x = 2`, `y = 2`  
**Output:** `[(1,1), (1,2), (1,3), (2,1), (2,3), (3,1), (3,2), (3,3)]`

### Example 2
**Input:** `x = 5`, `y = 7`  
**Output:** `[(6,7), (6,6), (6,8), (4,7), (4,6), (4,8), (5,6), (5,8)]`

## Notes

- The required data structure to contain the coordinates might not be the same between translations, so check the sample test cases provided
- Each point has exactly 8 neighboring points in a 2D grid
- The grid step is always 1

## Tags

`#Fundamentals` `#Mathematics`