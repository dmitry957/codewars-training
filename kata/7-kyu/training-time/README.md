# Training Time

**Kata Link:** [https://www.codewars.com/kata/572ab0cfa3af384df7000ff8/python](https://www.codewars.com/kata/572ab0cfa3af384df7000ff8/python)

## Problem Description

Create a function `shuffleIt`. The function accepts two or more parameters:

- **First parameter**: `arr` - an array of numbers
- **Additional parameters**: An arbitrary number of numeric arrays

Each numeric array contains two numbers, which are indices for elements in `arr` (the numbers will always be within bounds). For every such array, swap the elements.

## Requirements

Try to use all your new skills:
- Arrow functions
- The spread operator
- Destructuring
- Rest parameters

## Examples

```javascript
shuffleIt([1,2,3,4,5], [1,2]) 
// should return [1,3,2,4,5]

shuffleIt([1,2,3,4,5], [1,2], [3,4]) 
// should return [1,3,2,5,4]

shuffleIt([1,2,3,4,5], [1,2], [3,4], [2,3]) 
// should return [1,3,5,2,4]
```

## Tags

`#Fundamentals` `#Tutorials`