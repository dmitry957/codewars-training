# Cat and Mouse - 2D Version

[Codewars Kata Link](https://www.codewars.com/kata/57f8842367c96a89dc00018e/python)

## Description

You will be given a string (map) featuring a cat `"C"` and a mouse `"m"`. The rest of the string will be made up of dots (`"."`). The cat can move the given number of moves up, down, left or right, but not diagonally.

You need to find out if the cat can catch the mouse from its current position and return `"Caught!"` or `"Escaped!"` respectively.

Finally, if one of two animals are not present, return `"boring without two animals"`.

## Examples

**moves = 5**

```
map =
..C......
.........
....m....
```

returns `"Caught!"` because the cat can catch the mouse in 4 moves

**moves = 5**

```
map =
.C.......
.........
......m..
```

returns `"Escaped!"` because the cat cannot catch the mouse in 5 moves

#Graph Theory #Algorithms