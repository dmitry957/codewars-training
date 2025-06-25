# All Nines

[View on Codewars](https://www.codewars.com/kata/664b9dd610985cc3b6784111/python)

## Task

Given any positive integer `x` (where `x \leq 4000`), find the smallest positive integer `m` such that `m * x` consists of all 9's. Return `-1` if no such `m` exists.

### Examples

- `11 -> 9`, because `11 * 9 == 99`.
- `12 -> -1`, because 12 is even, so no multiple of it can contain only nines.
- `13 -> 76923`, because `13 * 76923 == 999999`, and no smaller positive integer, when multiplied by 13, generates an integer containing only nines.

**NOTE:** Although `x \leq 4000`, `m` can be very, very large. Where necessary, the way of handling big integers appropriate to the language should be used.

---

#Mathematics