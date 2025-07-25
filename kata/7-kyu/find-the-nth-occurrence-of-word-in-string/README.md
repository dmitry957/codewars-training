# Find the nth occurrence of a word in a string!

[Source](https://www.codewars.com/kata/5b1d1812b6989d61bd00004f/python)

## Description
You are required to implement a function that returns the index of the nth occurrence of a substring within a string (considering that those substring could overlap each other). If there are less than n occurrences of the substring, return -1.

## Example
**substring = "example"**
**string = "This is an example. Return the nth occurrence of example in this example string."**

```
substring, string, 1 --> 11
substring, string, 2 --> 49
substring, string, 3 --> 65
substring, string, 4 --> -1
```

Multiple occurrences of a substring are allowed to overlap, e.g.

**substring = "TestTest"**
**string = "TestTestTestTest"**

```
substring, string, 1 --> 0
substring, string, 2 --> 4
substring, string, 3 --> 8
substring, string, 4 --> -1
```

## Tags

#Fundamentals