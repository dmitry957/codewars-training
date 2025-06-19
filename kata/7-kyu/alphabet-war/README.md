# [Alphabet War](https://www.codewars.com/kata/59377c53e66267c8f6000027/python)

## Introduction
There is a war and nobody knows – the alphabet war!
There are two groups of hostile letters. The tension between left side letters and right side letters was too high and the war began.

## Task
Write a function that accepts a fight string consisting of only lowercase letters and returns who wins the fight:
- When the left side wins, return `Left side wins!`
- When the right side wins, return `Right side wins!`
- In other cases, return `Let's fight again!`

## Letter Powers
**The left side letters and their power:**

- `w` – 4
- `p` – 3
- `b` – 2
- `s` – 1

**The right side letters and their power:**

- `m` – 4
- `q` – 3
- `d` – 2
- `z` – 1

The other letters don't have power and are only victims. Sum up each side's letters' power values to determine which side wins.

## Example
```python
AlphabetWar("z")        # => Right side wins!
AlphabetWar("zdqmwpbs") # => Let's fight again!
AlphabetWar("zzzzs")    # => Right side wins!
AlphabetWar("wwwwwwz")  # => Left side wins!
```

#Fundamentals #Strings