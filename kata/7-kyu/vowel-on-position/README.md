# [Is it a vowel on this position?](https://www.codewars.com/kata/5a2b7edcb6486a856e00005b/python)

## Task
Check if there is a vowel (`a`, `e`, `i`, `o`, `u`) at the `n`-th position in a string (the first argument). Don't forget about uppercase vowels.

## Details
- The function should return `true` if the character at position `n` is a vowel (case-insensitive).
- If the position does not exist in the string, return `false`.
- If `n < 0`, return `false`.

## Examples
```javascript
checkVowel('cat', 1)  // true  ('a' is a vowel)
checkVowel('cat', 0)  // false ('c' is not a vowel)
checkVowel('cat', 4)  // false (this position doesn't exist)
checkVowel('Apple', 0) // true  ('A' is a vowel)
checkVowel('dog', -1) // false (n < 0)
```

#Fundamentals #Strings