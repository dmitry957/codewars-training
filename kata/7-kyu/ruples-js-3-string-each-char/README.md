# RuplesJS #3: String EachChar

[Link to Kata](https://www.codewars.com/kata/56808724e7784d220c00003f/python)

## Description

Your team is really excited with all the contributions you've made to the RuplesJS library. They feel the work you're doing will truly help Ruby developers transition to Javascript! They've assigned you another task.

### String.eachChar()
In ruby you can add something after each character in a string like so:

```
"hello".each_char {|c| print c, ' ' } -> "h e l l o " 
```

In the spirit of polymorphism, our eachChar method will allow one of two arguments, a callback function or a string. If a string is presented, it will be added after each character of the original string and return the new string. If a function is presented, it will perform a manipulation of each character in the string.

### Example:

```
each_char("hello"," ")
-> "h e l l o "

def func(c):
    return 'L' if c=='l' else c
    
each_char("hello all", func)
-> "heLLo aLL"
```

#Fundamentals #Language Features