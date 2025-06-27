# Linked Lists - Push & BuildOneTwoThree

[Codewars Kata Link](https://www.codewars.com/kata/55be95786abade3c71000079/python)

Write `push()` and `buildOneTwoThree()` functions to easily update and initialize linked lists. Try to use the `push()` function within your `buildOneTwoThree()` function.

Here's an example of `push()` usage:

```python
chained = None
chained = push(chained, 3)
chained = push(chained, 2)
chained = push(chained, 1)
push(chained, 8)  # 8 -> 1 -> 2 -> 3 -> None
```

The `push` function accepts `head` and `data` parameters, where `head` is either a node object or `None`. Your `push` implementation should be able to create a new linked list/node when `head` is `None`.

The `buildOneTwoThree` function should create and return a linked list with three nodes: `1 -> 2 -> 3 -> None`

---

#Linked Lists #Fundamentals