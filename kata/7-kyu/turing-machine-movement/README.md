# Turing Machine: Movement

[Codewars Link](https://www.codewars.com/kata/6885f0a045008e707baa714b/python)

## Description

In 1936, Alan Turing introduced the concept of a "universal machine": a theoretical device that could simulate any computation with a simple set of instructions and infinite tape. One of the simplest possible forms of computer.

[Computerphile Video](https://www.youtube.com/watch?v=dNRDvLACg5Q) | [Wikipedia](https://en.wikipedia.org/wiki/Turing_machine)

At each step, a Turing Machine needs to decide three things:

- what bit (0 or 1) to leave at the current position*
- where next to move on the tape
- which state to enter next*

It does this based on the current state*, and the bit at the current position.

\* = we don't worry about these in this kata

## Your task

In this kata, you will simulate movement of a Turing Machine in isolation.

You will be given:

- `tape`: a string of 1s and 0s
- `head`: the starting position on the tape
- `moves`: a string of left (`<`) and right (`>`) movements

Your function should simulate moving the head according to moves, and should return a string of 1s and 0s at the position of the head at the beginning of each step.

## Example

Given inputs:

```
tape: 011010
head: 3
moves: >><<
```

The output should be: `0101`.

Let's look at it step by step:

We start at the 0, the 3rd (0-indexed) bit (0 or 1) from the left, which we read, and move >.
We read the 1, and move > again.
We read another 0 and move <.
We read another 1, and move < again.
We're out of moves, and can return our output: the bits we read along the way (the last 4 bits in this case).

```
     : start  | step 1 | step 2 | step 3 | end     : read path
tape : 011010 | 011010 | 011010 | 011010 | 011010  :    1    >
head :    ^   |     ^  |      ^ |     ^  |    ^    :     0   >
move :    >   |     >  |      < |     <  |         :      1  <
read : 0      | 01     | 010    | 0101   | 0101    :     0   <
```

## Constraints

- You will never be given moves that take you outside the tape, so don't worry about that.
- The tape will have at most 100 bits, and you will be given at most 20 moves to simulate.

#State Machines