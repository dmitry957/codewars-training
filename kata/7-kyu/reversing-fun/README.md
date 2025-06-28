# Reversing Fun

**Kata Link:** [https://www.codewars.com/kata/566efcfbf521a3cfd2000056/python](https://www.codewars.com/kata/566efcfbf521a3cfd2000056/python)

## Description

You are going to be given a string. Your job is to return that string in a certain order that I will explain below:

## Process

Let's say you start with this: `"012345"`

1. The first thing you do is reverse it: `"543210"`
2. Then you will take the string from the 1st position and reverse it again: `"501234"`
3. Then you will take the string from the 2nd position and reverse it again: `"504321"`
4. Then you will take the string from the 3rd position and reverse it again: `"504123"`

Continue this pattern until you have done every single position, and then you will return the string you have created. For this particular number, you would return: `"504132"`

## Input/Output

**Input:** A string of length 1 - 1000

**Output:** A correctly reordered string.

## Tags

`#Strings` `#Fundamentals` `#Algorithms`