# Risk (Game): Battle Outcome

[View on Codewars](https://www.codewars.com/kata/581a825154f4dba286000014/python)

---

## Background
The boardgame Risk, published by Hasbro, Parker Brothers, and others since the late 1950s, is a game of global domination or world conquest.

Battles between opposing players are fought as combats in which, in the standard version of the game, the attacker rolls between 1 and 3 six-sided dice and the defender rolls either 1 or 2 six-sided dice.

The attacking and defending players' dice are paired up in order from highest to lowest, and the dice in each pair are compared against each other:
- If the attacker's die is greater than the defender's die, the defender loses one troop or army unit.
- If the attacker's die is less than or equal to the defender's die, the attacker loses one troop or army unit.
- Any remaining unpaired dice are ignored.

---

## Example
The attacking player's die rolls are: `2, 6, 4`  
The defending player's die rolls are: `5, 4`

- The attacker's highest die roll of 6 is paired with the defender's highest die roll of 5, and the defending player loses a unit.
- The attacker's next highest die roll of 4 is paired with defender's remaining die roll of 4, and the attacking player loses a unit.
- The attacker's lowest die roll of 2 is ignored.

---

## Task
Write a function which receives as inputs two arrays: one containing the attacker's die rolls in no particular order; the other the defender's die rolls, again in no particular order, and returns the result of the battle as a two-element array/tuple containing the numbers of units lost by the attacker and the defender respectively.

Some players who find the standard game a bit too slow-paced have adopted house rules for big battles in which one or both players may be permitted to roll more than 2 or 3 dice at the same time. The function should provide for this situation, and return an appropriate outcome to the big battle.

---

**Tags:** `#Fundamentals`