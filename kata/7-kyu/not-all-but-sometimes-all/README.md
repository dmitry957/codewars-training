# Not all but sometimes all

[Codewars Kata Link](https://www.codewars.com/kata/564ab935de55a747d7000040/python)

Write a function:

```python
remove(text, what)
```

that takes in a string `text` and a dictionary `what`, and returns a string with the chars removed as specified in `what`.

For example:

```python
remove('this is a string', {'t': 1, 'i': 2}) == 'hs s a string'
# remove from 'this is a string' the first 1 't' and the first 2 i's.

remove('hello world', {'x': 5, 'i': 2}) == 'hello world'
# there are no x's or i's, so nothing gets removed

remove('apples and bananas', {'a': 50, 'n': 1}) == 'pples d bnns'
# we don't have 50 a's, so just remove it till we hit end of string.
```

---

#Strings #Fundamentals