# Numbers Which Sum of Powers of Its Digits Is The Same Number

[Codewars Kata Link](https://www.codewars.com/kata/560a4962c0cc5c2a16000068/python)

Not considering number 1, the integer **153** is the first integer having this property: the sum of the third-power of each of its digits is equal to 153. Take a look:

153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153

The next number that exhibits this particular behaviour is **370** with the same power.

---

## Task

Write the function `eq_sum_powdig()`, that finds the numbers below a given upper limit `hMax` (inclusive) that fulfill this property but with different exponents as the power for the digits.

**Function signature:**

```python
eq_sum_powdig(hMax, exp)  # returns a sorted list of numbers (excluding 1)
```

---

## Examples

```python
eq_sum_powdig(100, 2)    # ➞ []
eq_sum_powdig(1000, 2)   # ➞ []
eq_sum_powdig(200, 3)    # ➞ [153]
eq_sum_powdig(370, 3)    # ➞ [153, 370]
```

---

**Tags:** #Fundamentals #Mathematics #DataStructures