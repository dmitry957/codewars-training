# Fusion Chamber Shutdown

[View on Codewars](https://www.codewars.com/kata/5fde1ea66ba4060008ea5bd9/python)

---

A laboratory is testing how atoms react in ionic state during nuclear fusion. They introduce different elements with Hydrogen in a high temperature and pressurized chamber. Due to an unknown reason, the chamber lost its power and the elements in it started precipitating.

Given the number of atoms of Carbon `[C]`, Hydrogen `[H]`, and Oxygen `[O]` in the chamber, calculate how many molecules of Water `[H2O]`, Carbon Dioxide `[CO2]`, and Methane `[CH4]` will be produced following the order of reaction affinity below:

1. Hydrogen reacts with Oxygen   = H₂O
2. Carbon   reacts with Oxygen   = CO₂
3. Carbon   reacts with Hydrogen = CH₄

---

## Example
```python
(C, H, O) = (45, 11, 100)
# return number of water, carbon dioxide, and methane molecules
# Output:
(5, 45, 0)
```

---

**Tags:** `#Fundamentals`