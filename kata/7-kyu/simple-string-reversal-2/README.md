# Simple String Reversal II - 7 kyu

## Kata Description

In this Kata, you will be given a string and two indexes (a and b). Your task is to reverse the portion of that string between those two indices inclusive.

## Examples

```python
str = "codewars", a = 1, b = 5 --> "cawedors"
str = "cODEWArs", a = 1, b = 5 --> "cAWEDOrs"
```

**Explanation:**
- For `"codewars"` with indices 1-5: reverse substring `"odewa"` → `"awe do"` → result: `"cawedors"`
- For `"cODEWArs"` with indices 1-5: reverse substring `"ODEWA"` → `"AWEDO"` → result: `"cAWEDOrs"`

## Constraints

Input will be lowercase and uppercase letters only.

The first index a will always be smaller than the string length; the second index b can be greater than the string length. More examples in the test cases. Good luck!

## Tags

`#Algorithms`