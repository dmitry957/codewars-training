# Tiling a rectangle with squares

[Codewars Link](https://www.codewars.com/kata/6328770fdfffbe000f4bb280/python)

## Description

You have to cover a rectangular area (measuring `n x m` where `n` and `m` are positive integers) with square tiles. You have an unlimited supply of square tiles, but the lengths of the sides are all powers of 2 (`1 x 1`, `2 x 2`, `4 x 4`, `8 x 8`, etc.).
You must use the minimum number of tiles which will exactly cover the area.

For example, given an area measuring 13 x 11:

```
___________________________
|               |  4x4  |_|
|               |       |_|
|               |       |_|
|               |_______|_|
|    8x8        |  4x4  |_|
|               |       |_|
|               |       |_|
|_______________|_______|_|
|2x2|2x2|2x2|2x2|2x2|2x2|_|
|___|___|___|___|___|___|_|
|_|_|_|_|_|_|_|_|_|_|_|_|_|
```

We can exactly cover the required area with 32 tiles.

Write a function which takes as its inputs the length and width of the rectangular area to be tiled, and returns the minimum number of tiles required to exactly fill the area.

> Be aware that some very large areas will be tested.

#Fundamentals #Algorithms #Recursion #Performance