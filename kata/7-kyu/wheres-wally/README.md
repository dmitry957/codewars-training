# Where's Wally

**Kata Link:** [https://www.codewars.com/kata/55f91a98db47502cfc00001b/python](https://www.codewars.com/kata/55f91a98db47502cfc00001b/python)

## Description

Write a function that returns the index of the first occurrence of the word "Wally".

## Rules

- "Wally" must not be part of another word
- It can be directly followed by a punctuation mark
- If no such "Wally" exists, return -1

## Examples

```python
"Wally" --> 0
"Where's Wally" --> 8
"Where's Waldo" --> -1
"DWally Wallyd .Wally" --> -1
"Hi Wally." --> 3
"It's Wally's." --> 5
"Wally Wally" --> 0
"'Wally Wally" --> 7
```

## Tags

`#Regular Expressions` `#Fundamentals`