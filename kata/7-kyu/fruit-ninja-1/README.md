# I Guess This is a 7kyu Kata #6: Fruit Ninja I

[View on Codewars](https://www.codewars.com/kata/57d60363a65454701d000e11/python)

You are a Fruit Ninja, your skill is cutting fruit. All the fruit will be cut in half by your knife. For example:

```python
["apple", "pear", "banana"]  # --> ["app", "le", "pe", "ar", "ban", "ana"]
```

As you see, all fruits are cut in half. You should pay attention to "apple": if you cannot cut a fruit into equal parts, then the first part will have an extra character.

You should only cut the fruit; other things should not be cut, such as the "bomb":

```python
["apple", "pear", "banana", "bomb"]  # --> ["app", "le", "pe", "ar", "ban", "ana", "bomb"]
```

The valid fruit names are preloaded for you as:

`FRUIT_NAMES`

## Task

Complete function `cut_fruits` that accepts argument `fruits`. Returns the result in accordance with the rules above.

---

#Puzzles