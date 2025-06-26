# Talisman Board Game Combat System Checker

[View on Codewars](https://www.codewars.com/kata/541837036d821665ee0006c2/python)

---

In the board game Talisman, when two players enter combat the outcome is decided by a combat score, equal to the player's power plus any modifiers plus the roll of a standard 1-6 dice. The player with the highest combat score wins and the opposing player loses a life. In the case of a tie, combat ends with neither player losing a life.

---

## Example

```
Player 1: 5 Power, 0 Modifier
Player 2: 3 Power, 2 Modifier

Player 1 rolls a 4, Player 2 rolls a 2.

(5 + 0 + 4) -> (3 + 2 + 2)
Player 1 wins (9 > 7)
```

---

## Task
Write a method that calculates the required roll for the player to win.

The player and enemy stats are given as an array in the format:

```
[power, modifier]
```

For example, for the examples used above the stats would be given as:

```python
get_required([5, 0], [3, 2]) # returns 'Random'
```

---

## Rules
- If the player has at least 6 more power (including modifiers) than the enemy, they automatically win the fight, as the enemy's combat score couldn't possibly exceed the player's. Return **"Auto-win"**.
  - Example: `get_required([9, 0], [2, 1]) # returns 'Auto-win'`
- If the enemy has at least 6 more power (including modifiers) than the player, they automatically win the fight. Return **"Auto-lose"**.
  - Example: `get_required([2, 1], [9, 0]) # returns 'Auto-lose'`
- If the player and enemy have the same power (including modifiers), the outcome is purely down to the dice roll. Return **"Random"**.
  - Example: `get_required([5, 0], [3, 2]) # returns 'Random'`
- If the player has greater power than the enemy (including modifiers), the player could guarantee a win by rolling a high enough number on the dice. Return a range equal to the numbers which would guarantee victory for the player.
  - Example: `get_required([6, 0], [2, 2]) # returns '(5..6)'`
  - Example: `get_required([7, 1], [2, 2]) # returns '(3..6)'`
- If the player has less power than the enemy (including modifiers), the player can only win if the enemy rolls a low enough number, providing they then roll a high enough number. Return a range equal to the numbers which would allow the player a chance to win.
  - Example: `get_required([4, 0], [6, 0]) # returns '(1..3)'`
  - Example: `get_required([1, 1], [6, 0]) # returns '(1..1)'`
- If the best case scenario for the player is to hope for a tie, then return **"Pray for a tie!"**.
  - Example: `get_required([7, 2], [6, 8]) # returns 'Pray for a tie!'`

---

**Tags:** `#Games` `#Algorithms`