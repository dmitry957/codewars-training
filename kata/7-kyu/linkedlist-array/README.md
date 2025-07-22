# LinkedList -> Array

<https://www.codewars.com/kata/557dd2a061f099504a000088/python>

## Description

Linked lists are data structures composed of nested or chained objects, each containing a single value and a reference to the next object.

Here's an example of a list:

```python
class LinkedList:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
        
LinkedList(1, LinkedList(2, LinkedList(3)))
```

Write a function `listToArray` (or `list_to_array` in Python) that converts a list to an array, like this:

```json
[1, 2, 3]
```

Assume all inputs are valid lists with at least one value. For the purpose of simplicity, all values will be either numbers, strings, or Booleans.

---
*Data Structures, Arrays, Fundamentals*