# How many points did the teams from Los Angeles score?

<https://www.codewars.com/kata/580559b17ab3396c58000abb/python>

## Description

You are given an array including a list of basketball teams and their scores showing points scored vs points lost:

```python
[
  ["Dallas Mavericks", "492:513"],
  ["Los Angeles Lakers", "641:637"],
  ["Houston Rockets", "494:458"],
  ["Los Angeles Clippers", "382:422"],
  ["New Orleans Pelicans", "433:454"],
  ["Oklahoma City Thunder", "315:318"],
  ["Golden State Warriors", "559:503"],
  ["Memphis Grizzlies", "550:511"],
  ["Portland Trail Blazers", "527:520"],
  ["Minnesota Timberwolves", "495:494"],
  ["Utah Jazz", "399:402"],
  ["Sacramento Kings", "420:431"],
  ["San Antonio Spurs", "469:460"],
  ["Phoenix Suns", "523:522"],
  ["Denver Nuggets", "646:658"]
]
```

Your task is to return a number that represents the total number of points scored by a team from Los Angeles.

In the above example, the correct result is a number of 1023, as Los Angeles Lakers got 641 and Los Angeles Clippers got 382, so 641 + 382 = 1023.

### Notes:

- The format of the Los Angeles team name always starts with "Los Angeles," followed by a one-word team name, for example, "Los Angeles Name". 
- Each word in the Los Angeles team name must be at least two letters long and capitalized, that is, one uppercase letter followed by one or more lowercase letter. Only letters are used (no numbers, underscores, hyphens, special characters, etc.)
- For example, the following strings do not represent a team from Los Angeles: "Happy Los Angeles", "Los Angeles", "Los Angelesio Thunders", "los angeles masters", "Los Angeles M".
- The number of teams from Los Angeles may vary.
- If there are no teams from Los Angeles, return the number 0.
- The order of the teams may vary.
- All values in the arrays will always be strings.
- Points will always be given in the following format: "100:99" (points scored:points lost).

---
*Algorithms, Data Structures, Arrays, Regular Expressions*