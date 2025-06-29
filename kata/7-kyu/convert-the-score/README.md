# Convert the Score

**Kata Link:** [https://www.codewars.com/kata/5b6c220fa0a661fbf200005d/python](https://www.codewars.com/kata/5b6c220fa0a661fbf200005d/python)

## Problem Description

You are working at a lower league football stadium and you've been tasked with automating the scoreboard.

The referee will shout out the score, you have already set up the voice recognition module which turns the ref's voice into a string, but the spoken score needs to be converted into a pair for the scoreboard!

## Task

Create a function that converts spoken score descriptions into a numerical array format.

## Examples

### Example 1
**Input:** `"The score is four nil"`  
**Output:** `[4, 0]`

### Example 2
**Input:** `"new score: two three"`  
**Output:** `[2, 3]`

### Example 3
**Input:** `"two two"`  
**Output:** `[2, 2]`

### Example 4
**Input:** `"Arsenal just conceded another goal, two nil"`  
**Output:** `[2, 0]`

## Requirements

- Either team's score has a range of 0-9
- The referee won't say the same string every time
- The function should extract the numerical scores from various spoken formats
- Return an array with two numbers representing the scores

## Notes

- Please return an array
- The input string can contain various text around the actual scores
- You need to identify and extract the numerical values from the spoken words

## Tags

`#Fundamentals` `#Arrays`