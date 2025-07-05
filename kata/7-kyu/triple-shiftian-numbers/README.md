# Triple Shiftian Numbers

**URL:** https://www.codewars.com/kata/56b7526481290c2ff1000c75/python

## Description

Much cooler than your run-of-the-mill Fibonacci numbers, the Triple Shiftian are so defined: `T[n] = 4 * T[n-1] - 5 * T[n-2] + 3 * T[n-3]`.

You are asked to create a function which accept a base with the first 3 numbers and then returns the nth element.

### Examples

- Given `base=[1,1,1]`, `n=25` ==> `1219856746`
- Given `base=[1,2,3]`, `n=25` ==> `2052198929`
- Given `base=[6,7,2]`, `n=25` ==> `-2575238999`
- Given `base=[3,2,1]`, `n=35` ==> `23471258855679`
- Given `base=[1,9,2]`, `n=2`  ==> `2`

---

**Tags:** #Number Theory #Fundamentals