# Valid HK Phone Number

**Kata Link:** [https://www.codewars.com/kata/56f54d45af5b1fec4b000cce/python](https://www.codewars.com/kata/56f54d45af5b1fec4b000cce/python)

## Overview

In Hong Kong, a valid phone number has the format `xxxx xxxx` where `x` is a decimal digit (0-9).

## Format Rules

- Must be exactly 8 digits
- Must have exactly 1 space separating the first 4 and last 4 digits
- Each digit must be 0-9

## Examples

### Valid Phone Numbers

```python
"1234 5678"    # is valid
"2359 1478"    # is valid
```

### Invalid Phone Numbers

```python
"85748475"     # invalid, as there are no spaces separating the first 4 and last 4 digits
"3857  4756"   # invalid; there should be exactly 1 whitespace separating the first 4 and last 4 digits respectively
"sklfjsdklfjsf" # clearly invalid
```

### Strings Containing Valid Phone Numbers

```python
"     1234 5678   "    # is NOT a valid phone number but CONTAINS a valid phone number
"skldfjs287389274329dklfj84239029043820942904823480924293042904820482409209438dslfdjs9345 8234sdklfjsdkfjskl28394723987jsfss2343242kldjf23423423SDLKFJSLKsdklf"  # also contains a valid HK phone number (9345 8234)
```

## Task

Define two functions that return whether a given string:
1. **Is** a valid HK phone number
2. **Contains** a valid HK phone number

Both functions should return true/false values.

## Tags

`#Regular Expressions` `#Fundamentals`