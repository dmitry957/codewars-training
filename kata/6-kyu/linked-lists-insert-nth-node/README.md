# Linked Lists - Insert Nth Node

[Codewars Link](https://www.codewars.com/kata/55cacc3039607536c6000081/python)

## Description

### Linked Lists - Insert Nth

Implement a function which inserts a new node at any index within a list.

Given a list, an index `n` in the range `0..length`, and a data element, insert a node in list at index `n` containing data. Your function should return the head of the list.

```
list            n data
(1 -> 2 -> 3 -> null, 0, 7) ==> 7 -> 1 -> 2 -> 3 -> null
(1 -> 2 -> 3 -> null, 1, 7) ==> 1 -> 7 -> 2 -> 3 -> null
(1 -> 2 -> 3 -> null, 3, 7) ==> 1 -> 2 -> 3 -> 7 -> null
```

You must throw/raise an exception if the index is too large.

#Linked Lists #Data Structures #Fundamentals