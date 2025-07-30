# [Code Golf] - ZeroFiller

[Codewars Link](https://www.codewars.com/kata/6777397b65316bd17df0f678/train/python)

## Description

You need to create a function `f(n, l)` that takes two inputs:

- **n**: A value that can be one of the following types:
  - A string
  - An integer (positive or negative)
  - A boolean (True or False)
- **l**: An integer representing the desired minimum length of the output.

The function must return a string of length `l` by padding `n` with zeroes (`0`) in a specific way based on the input type. If the length of `n` is greater than or equal to `l`, it should return `n` unchanged.

### Behavior

If `n` is:

- **A string**: Pad it with trailing zeroes (`0`) from the right until its length equals `l`.
- **A positive or negative number**: Convert it to a string and pad with leading zeroes (`0`) from the left (after the sign for negatives) until its length equals `l`.
- **A boolean**: Convert it to `1` for `True` and `0` for `False`, then pad with leading zeroes (`0`) from the left until its length equals `l`.

If the length of `n` is greater than or equal to `l`, return `n` as-is without truncation.

### Constraints

- `l` will always be greater than or equal to the desired length of `n` when padding is applied.
- The solution must be a code golf style, with a maximum length of 25 characters.

### Examples

```python
f('-122121', 5)  # "-122121"
f(122121, 5)     # "122121"
f(-122121, 5)    # "-122121"
f(12, 5)         # "00012"
f('ab', 5)       # "ab000"
f(True, 5)       # "00001"
f(False, 5)      # "00000"
```

#Strings #Fundamentals