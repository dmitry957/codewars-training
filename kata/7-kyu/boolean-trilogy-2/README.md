# [Boolean Trilogy #2: Calculate Boolean Expression (Easy)](https://www.codewars.com/kata/5f8070c834659f00325b5313/train/python)

## Task
You get a Boolean expression and the values of its variables as input. Your task is to calculate this Boolean expression with a given set of variable values.

## Details
- The input expression consists of variables represented by uppercase letters `A-F` and operations `&` (logical AND) and `|` (logical OR).
- Parentheses and other operations are **not** present in the expression.
- Variables can be repeated and placed in any order.
- The expression contains at least one variable.
- Variable values are represented as a dictionary `{name: value}`.

## Examples
```python
calculate("A & B & C", {"A": 0, "B": 1, "C": 0})   # returns 0
# A & B & C = 0 & 1 & 0 = 0

calculate("B & A | C", {"A": 1, "B": 0, "C": 1})   # returns 1
# B & A | C = 0 & 1 | 1 = 0 | 1 = 1
```

#Fundamentals