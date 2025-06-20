# Clean Nesting Tree

[View on Codewars](https://www.codewars.com/kata/67c9c1cdf96c66388eb35cd4/python)

## Task

You are given a main list that may contain nested lists of arbitrary depth. Imagine this structure as a tree, where each list is a node and its elements are child nodes.

Your task is to implement a function that checks whether the entire structure follows the nesting rule.

### Nesting Rule
At each level (depth) of the tree, each node's children must all be **either**:
- dead ends (empty lists `[]`)
- nested lists (lists containing other lists)

## Examples

- `[ [ [[]], [[]], [[]]  ], [[]] , [[]]  ]` -> `True`
- `[]` -> `True`
- `[ [], [] ]` -> `True`

---

- `[ [ [], [], []  ] , [ [], [[]]  ] ]` -> `False`
  - **Explanation:** Look at the list at index 1 in the main list: `[ [], [[]] ]`. It contains two lists: `[]` and `[[]]`. One is a dead end and one is nested. This violates the nesting rule.

- `[ [ [ [[]],[[]]  ], [[]] ] , [ [] ] ]` -> `True`

- `[ [ [ [[]], [[]], []  ], [[]] ] , [ [] ] ]` -> `False`
  - **Explanation:**
    1. The first two lists in the main list are both nested, which is fine.
    2. We check the list at index 0: `[ [ [[]], [[]], [] ], [[]] ]`. It has two child lists: `[ [[]], [[]], [] ]` and `[[]]`. Both are nested, so this level is also fine.
    3. We go deeper into the first of these: `[ [[]], [[]], [] ]`. It has three child lists: `[[]]`, `[[]]`, and `[]`. This violates the rule because the first two are nested but the last one is a dead end. They must all be of the same type (either all nested or all dead ends).

- `[ [], [[], [], []] , [] ]` -> `False`
  - **Explanation:** The main list contains three lists: `[]`, `[[], [], []]`, and `[]`. Two are dead ends, but one is nested, which is inconsistent.

---

#Lists #Arrays #Recursion #Trees