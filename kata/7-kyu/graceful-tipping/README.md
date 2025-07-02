# Graceful Tipping

[Codewars Kata Link](https://www.codewars.com/kata/5eb27d81077a7400171c6820/python)

## Description

Adding tip to a restaurant bill in a graceful way can be tricky, that's why you need make a function for it.

The function will receive the restaurant bill (always a positive number) as an argument. You need to:

1. Add at least 15% in tip
2. Round that number up to an elegant value
3. Return it

**What is an elegant number?**

It depends on the magnitude of the number to be rounded. Numbers below 10 should simply be rounded to whole numbers. Numbers 10 and above should be rounded like this:

- **10 - 99.99...**  → Round to number divisible by 5
- **100 - 999.99...** → Round to number divisible by 50
- **1000 - 9999.99...** → Round to number divisible by 500
- And so on...

## Examples
```
 1  -->    2
 7  -->    9
12  -->   15
86  -->  100
```

#Mathematics #Fundamentals