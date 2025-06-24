# Enumerable Magic #5 - True for Just One?

[Codewars Kata Link](https://www.codewars.com/kata/54599705cbae2aa60b0011a4/python)

---

## Task

Create a function called `one` that accepts two parameters:

- a sequence
- a function

and returns `True` only if the function returns `True` for exactly one (1) item in the sequence.

---

## Example

```python
one([1, 3, 5, 6, 99, 1, 3], bigger_than_ten)  # ➞ True
one([1, 3, 5, 6, 99, 88, 3], bigger_than_ten) # ➞ False
one([1, 3, 5, 6, 5, 1, 3], bigger_than_ten)   # ➞ False
```

---

**Tags:** #Fundamentals