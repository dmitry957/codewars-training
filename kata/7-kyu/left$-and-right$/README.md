# Left$ and Right$

[Codewars Link](https://www.codewars.com/kata/53f211b159c3fcec3d000efa/python)

## Description
Once upon a time, more precisely upon BASIC time, there were 2 functions named LEFT$ and RIGHT$ (I wrote them uppercase because it was the custom in those early years).

These functions let you read left(/right)-most characters of a string.

use: `LEFT$ (str, i)` -> returns i left-most characters of str.
- eg:
```basic
A$="ABCDEFG":PRINT LEFT$(A$,3)  ' prints ABC
```
and `RIGHT$ (str, i )`, of course, returns i right-most characters of str.

So, your mission is...
...to write 2 functions (`left$(str, i)` & `right$(str, i)`) (`left` & `right` in Ruby or Python) that will work as the BASIC ones did,... except :

- i may be a negative integer. In this case the function returns the whole string but i right(/left)-most chars (respectively in left$(/right$) function).
- if i === 0 : returns an empty string;
- if no i is provided consider it should be 1 ( not zero ).
- if i is greater than str length : returns the whole str.

and

- if i is a string ( yes it can ) : returns part of str at left(/right) of i.
  - returns left of first occurence of i
  - returns right of last occurence of i

## Examples
```python
text = 'Hello (not so) cruel World!'

left(text,5)   # -> 'Hello'
left(text,-22) # -> 'Hello'
left(text,1)   # -> 'H'
left(text)     # -> 'H' too
left(text,0)   # -> ''
left(text,99)  # -> 'Hello (not so) cruel World!'

right(text,6)  # -> 'World!'
right(text)    # -> '!'

#== with string as 2nd argument ==
left(text,'o') # -> 'Hell'
right(text,'o')# -> 'rld!'
left(text,' ') # -> 'Hello'  # -- string may be a space
```

---

#Strings #Fundamentals