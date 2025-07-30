# 12 days of Christmas (REAL TOTALS)

[Codewars Link](https://www.codewars.com/kata/676474a0956b84eab4132819/python)

## Description

Have you ever really thought about the song “The Twelve Days of Christmas”? On the first day, you receive a “partridge in a pear tree.” Then on the second day, you receive another “partridge in a pear tree” along with two “turtle doves.” This pattern continues, so by the third day, you get another partridge in a pear tree, another two turtle doves, and three “French hens.” The gifts keep piling up!

So, how many of each gift would you receive by the end if you kept receiving all the gifts from the starting day onward?

## Problem Description

In this Kata, you will be given a list of items. Your task is to calculate how many of each item you would receive if the pattern followed the song.

**Assume:**

- On day 1, you get 1 of the first item.
- On day 2, you get 2 of the second item, and so on.
- Each item is delivered daily from its starting day onward.

### Example

```python
Input -> items = ["tree", "bows", "birds", "candy"]
```

**Explanation:**

- "tree" starts on day 1: 1 tree on day 1, 1 tree on day 2, 1 tree on day 3, and 1 tree on day 4 → 4 trees total.
- "bows" starts on day 2: 2 bows on day 2, 2 bows on day 3, and 2 bows on day 4 → 6 bows total.
- "birds" starts on day 3: 3 birds on day 3 and 3 birds on day 4 → 6 birds total.
- "candy" starts on day 4: 4 candies on day 4 → 4 candies total.

```python
Output -> ['4 tree', '6 bows', '6 birds', '4 candy']
```

**Notes:**

- The output should include the total count of each item, followed by the item name, separated by a space (no need to pluralize the item names).
- The input list will contain between 3 and 24 items.