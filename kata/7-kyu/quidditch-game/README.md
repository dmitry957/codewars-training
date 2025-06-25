# Gryffindor vs Slytherin Quidditch Game

[View on Codewars](https://www.codewars.com/kata/5840946ea3d4c78e90000068/python)

It's the most hotly anticipated game of the school year - Gryffindor vs Slytherin! Write a function which returns the winning team.

You will be given two arrays with two values:
- The first value is the number of points scored by the team's Chasers.
- The second is a string with a `'yes'` or `'no'` value indicating if the team caught the golden snitch.

The team who catches the snitch wins their team an extra 150 points - but doesn't always win them the game.

## Examples

```python
gameWinners([150, 'yes'], [200, 'no'])  # 'Gryffindor wins!'
gameWinners([400, 'no'], [350, 'yes'])  # 'Slytherin wins!'
```

If the score is a tie, return `"It's a draw!"`

**Note:** The game only ends when someone catches the golden snitch, so one array will always include `'yes'` or `'no'`. Points scored by Chasers can be any positive integer.

---

#Fundamentals