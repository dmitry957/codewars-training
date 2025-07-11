# Head, Tail, Init and Last

[View on Codewars](https://www.codewars.com/kata/54592a5052756d5c5d0009c3/python)

---

Haskell has some useful functions for dealing with lists:

```haskell
$ ghci
GHCi, version 7.6.3: http://www.haskell.org/ghc/  :? for help
λ head [1,2,3,4,5]
1
λ tail [1,2,3,4,5]
[2,3,4,5]
λ init [1,2,3,4,5]
[1,2,3,4]
λ last [1,2,3,4,5]
5
```

Your job is to implement these functions in your given language. Make sure it doesn't edit the array; that would cause problems! Here's a cheat sheet:

```
| HEAD | <----------- TAIL ------------> |
[  1,  2,  3,  4,  5,  6,  7,  8,  9,  10]
| <----------- INIT ------------> | LAST |
```

```haskell
head [x] = x
tail [x] = []
init [x] = []
last [x] = x
```

Here's how I expect the functions to be called in your language:

```python
head([1,2,3,4,5]) => 1
tail([1,2,3,4,5]) => [2,3,4,5]
```

Most tests consist of 100 randomly generated arrays, each with four tests, one for each operation. There are 400 tests overall. No empty arrays will be given. Haskell has QuickCheck tests.

---

**Tags:** `#Arrays` `#Lists` `#Fundamentals`