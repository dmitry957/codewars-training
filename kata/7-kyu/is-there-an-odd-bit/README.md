# Is There an Odd Bit?

[View on Codewars](https://www.codewars.com/kata/5d6f49d85e45290016bf4718/python)

---

Return `true` when any odd bit of `x` equals 1; `false` otherwise.

Assume that:
- `x` is an unsigned, 32-bit integer
- The bits are zero-indexed (the least significant bit is position 0)

## Examples

```python
2    -->  1 (true)  # at least one odd bit is 1 (2 = 0b10)
5    -->  0 (false) # none of the odd bits are 1 (5 = 0b101)
170  -->  1 (true)  # all of the odd bits are 1 (170 = 0b10101010)
```

---

**Tags:** `#Bits` `#Fundamentals`