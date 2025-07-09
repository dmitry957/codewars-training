# Simple Maths Test

[Codewars Kata Link](https://www.codewars.com/kata/5507309481b8bd3b7e001638/python)

## Description
Create a function which checks a number for three different properties.

- is the number prime?
- is the number even?
- is the number a multiple of 10?

Each should return either true or false, which should be given as an array. Remark: The Haskell variant uses data Property.

## Examples
```
number_property(7)  # ==> [true,  false, false] 
number_property(10) # ==> [false, true,  true] 
```
The number will always be an integer, either positive or negative. Note that negative numbers cannot be primes, but they can be multiples of 10:
```
number_property(-7)  # ==> [false, false, false] 
number_property(-10) # ==> [false, true,  true] 
```

#Algorithms #Mathematics