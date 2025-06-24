# Even Odd Disparity

[Codewars Kata Link](https://www.codewars.com/kata/59c62f1bdcc40560a2000060/python)

---

## Task

Given an array, return the difference between the count of even numbers and the count of odd numbers. `0` will be considered an even number.

---

## Examples

```python
solve([0, 1, 2, 3])  # ➞ 0
# There are two even numbers and two odd numbers. Even - Odd = 2 - 2 = 0.

solve([0, 1, 2, 3, 'a', 'b'])  # ➞ 0
# Even - Odd = 2 - 2 = 0. Ignore letters.
```

The input will be an array of lowercase letters and numbers only.

In some languages (Haskell, C++, and others), input will be an array of strings:

```haskell
solve ["0","1","2","3","a","b"]  -- ➞ 0
```

---

**Tags:** #Fundamentals