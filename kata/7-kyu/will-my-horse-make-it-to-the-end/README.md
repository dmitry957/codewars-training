# Will my horse make it to the end?

[Codewars Kata Link](https://www.codewars.com/kata/679e0a54f8d448b508865c3b/python)

You are a professional horse rider and you are about to have a ride on a horse over a line of obstacles. You have a very experienced eye and you can instantly give a rough estimate of the horse's stamina. Moreover, you learned how much stamina it would take for a horse to jump over a certain obstacle. The only problem now is to understand immediately if the given horse will actually overcome all of the obstacles before it runs out of energy! Your task is to help the horse rider to find it out.

## Task

Given the horse's stamina and a map representing the course, determine if the horse can reach the end without running out of energy.

Return `True` if the horse completes the course with stamina ≥ 0, otherwise return `False`.

## Input

- **stamina** (integer) – the horse's starting stamina.
- **map** (array of 0s and 1s) – represents the track:
  - `0` – flat ground (no stamina loss).
  - `1` – obstacle (requires stamina to jump).

## Stamina Cost per Obstacle

- A single `1` (length 1) costs **2 stamina**.
- A pair of consecutive `1`s (length 2) costs **5 stamina**.
- A triplet of consecutive `1`s (length 3) costs **10 stamina**.

## Examples

```python
[0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0], 18  # -> False
[1, 1], 5  # -> True
[0, 1, 0, 0, 0, 0, 1], 3  # -> False
```

---

#Lists #Arrays