# Grid blast!

[Codewars Kata Link](https://www.codewars.com/kata/54fdfe14762e2edf4a000a33/python)

## Description

Ready! Set! Fire... but where should you fire?

The battlefield is 3x3 wide grid. HQ has already provided you with an array for easier computing:

```python
["top left",    "top middle",    "top right",
 "middle left", "center",        "middle right",
 "bottom left", "bottom middle", "bottom right"]
```

HQ radios you with 'x' and 'y' coordinates. x=0 y=0 being 'top left' part of the battlefield;

Your duty is to create a function that takes those Xs and Ys and return the correct grid sector to be hit.

- x = 0, y = 0 --> "top left"
- x = 1, y = 2 --> "bottom middle"
- etc

#Fundamentals #Arrays