# Rigged Dice

[Link to Kata](https://www.codewars.com/kata/573acc8cffc3d13f61000533/python)

## Description
Create a rigged dice function that 22% of the time returns the number 6. The rest of the time it returns the integers 1,2,3,4,5 uniformly.

## About the test case

There will only be one test case which calls the throw_rigged function 100k times and checks that 6 is returned in the range of 21700-22300 (inclusive) times. The test does not check that 1-5 is returned uniformly or randomly, but it does check that your function returns integers in the range 1-6 (inclusive).

The test works roughly 98% of the time, so you might want to run it twice if you are confident your solution is correct.

#Probability #Refactoring