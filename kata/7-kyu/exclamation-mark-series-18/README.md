# Exclamation marks series #18: s simple slot machine that only contains exclamation marks and question marks

[View on Codewars](https://www.codewars.com/kata/57fb4b289610ce39f70000de/python)

You are playing a simple slot machine that only contains exclamation marks and question marks. Every time the slot machine is started, a string of length 5 is obtained. If you're lucky enough to get a special permutation, you'll win the bonus. Given a string `s`, return the highest bonus.

## Bonus List

- **Five-of-a-Kind**: 1000  
  `!!!!!` or `?????`
- **Four-of-a-Kind**: 800  
  The string contains `!!!!` or `????`  
  Examples: `!!!!?`, `?!!!!`, `????!`, `!????`
- **Full House**: 500  
  Examples: `!!!??`, `???!!`
- **Three-of-a-Kind**: 300  
  The string contains `!!!` or `???`  
  Examples: `!!!?!`, `!???!`
- **Two Pair**: 200  
  The string contains two `!!` or `??`  
  Examples: `??!!?`, `!!?!!`
- **A Pair**: 100  
  The string contains `!!` or `??`  
  Examples: `?!??!`, `!!?!?`
- **Others**: 0  
  Examples: `?!?!?`, `!?!?!`

## Examples

```python
slot("!!!!!") == 1000
slot("!!!!?") == 800
slot("!!!??") == 500
slot("!!!?!") == 300
slot("!!?!!") == 200
slot("!!?!?") == 100
slot("!?!?!") == 0
```

---

#Fundamentals