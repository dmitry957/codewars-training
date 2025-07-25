# PRNG: Linear Congruential Generator

[Codewars Kata Link](https://www.codewars.com/kata/594979a364becbc1ab00003a/python)

## Description
The Linear Congruential Generator (LCG) is one of the oldest pseudo random number generator functions.

The algorithm is as follows:

\[
X_{n+1} = (a \cdot X_n + c) \mod m
\]

where:

- `a`/`A` is the multiplier (we'll be using 2)
- `c`/`C` is the increment (we'll be using 3)
- `m`/`M` is the modulus (we'll be using 10)
- `X_0` is the seed.

## Your task
Define a method `random`/`Random` in the class `LCG` that provides the next random number based on a seed. You never return the initial seed value.

Similar to `random`, return the result as a floating point number in the range `[0.0, 1.0)`

## Example

```python
# initialize the generator with seed = 5
LCG(5)

# first random number (seed = 5)
LCG.random() = 0.3      # (2 * 5 + 3) mod 10 = 3 --> return 0.3

# next random number (seed = 3)
LCG.random() = 0.9      # (2 * 3 + 3) mod 10 = 9 --> return 0.9

# next random number (seed = 9)
LCG.random() = 0.1

# next random number (seed = 1)
LCG.random() = 0.5
```

---

*#Algorithms*