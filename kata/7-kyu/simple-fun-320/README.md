# Simple Fun #320: Scratch lottery I

[View on Codewars](https://www.codewars.com/kata/594a1822a2db9e93bd0001d4/python)

---

## Task
You got a scratch lottery, and you want to know how much money you win.

There are 6 sets of characters on the lottery. Each set of characters represents a chance to win. The text has a coating on it. When you buy the lottery ticket and then blow it off, you can see the text information below the coating.

Each set of characters contains three animal names and a number, like this: `"tiger tiger tiger 100"`. If the three animal names are the same, congratulations, you won the prize. You will win the same bonus as the last number.

Given the lottery, return the total amount of the bonus.

---

## Input/Output
- **Input:** `string[] lottery` — A string array that contains six sets of characters.
- **Output:** `integer` — The total amount of the bonus.

---

## Example

```python
lottery = [
  "tiger tiger tiger 100",
  "rabbit dragon snake 100",
  "rat ox pig 1000",
  "dog cock sheep 10",
  "horse monkey rat 5",
  "dog dog dog 1000"
]
# the output should be 1100.
```

- "tiger tiger tiger 100" wins $100
- "dog dog dog 1000" wins $1000

100 + 1000 = 1100

---

**Tags:** `#Puzzles` `#Regular Expressions`