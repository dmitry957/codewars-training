# String doubles

[Codewars Kata Link](https://www.codewars.com/kata/5a145ab08ba9148dd6000094/python)

## Description

In this Kata, you will write a function `doubles` that will remove double string characters that are adjacent to each other.

For example:

```python
doubles('abbcccdddda') = 'aca'  # from left to right:
# a) There is only one 'a' on the left hand side, so it stays.
# b) The 2 b's disappear because we are removing double characters that are adjacent.
# c) Of the 3 c's, we remove two. We are only removing doubles.
# d) The 4 d's all disappear, because we first remove the first double, and again we remove the second double.
# e) There is only one 'a' at the end, so it stays.

doubles('abbbzz') = 'ab'
doubles('abba') = ''  # when we remove the b's in 'abba', the double a that results is then removed.
```

The strings will contain lowercase letters only. More examples in the test cases.

---

#Strings #Algorithms