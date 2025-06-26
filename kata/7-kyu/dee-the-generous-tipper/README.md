# Dee, The Generous Tipper

[View on Codewars](https://www.codewars.com/kata/568c3498e48a0231d200001f/python)

---

Dee is lazy but she's kind and she likes to eat out at all the nice restaurants and gastropubs in town. To make paying quick and easy she uses a simple mental algorithm she's called The Fair 20% Rule. She's gotten so good she can do this in a few seconds and it always impresses her dates but she's perplexingly still single. Like you probably.

---

## This is how she does it:

1. **Round the price `P` at the tens place:**
    - 25 becomes 30
    - 24 becomes 20
    - 5 becomes 10
    - 4 becomes 0
2. **Figure out the base tip `T` by dropping the singles place digit:**
    - When P = 24 she rounds to 20, drops 0 → T = 2
    - P = 115 rounds to 120, drops 0 → T = 12
    - P = 25 rounds to 30, drops 0 → T = 3
    - P = 5 rounds to 10, drops 0 → T = 1
    - P = 4 rounds to 0 → T = 0
3. **Apply a 3-point satisfaction rating `R` to `T`:**
    - When she's satisfied: R = 1, she'll add 1 to T
    - Unsatisfied: R = 0, she'll subtract 1 from T
    - Appalled: R = -1, she'll divide T by 2, round down, and subtract 1

---

## Your Task
Implement a method `calc_tip` that takes two integer arguments for price `p` (where 1 ≤ p ≤ 1000) and a rating `r` which is one of -1, 0, 1.

The return value `T` should be a non-negative integer.

**Note:** Each step should be done in the order listed.

---

**Tags:** `#Mathematics` `#Algorithms`