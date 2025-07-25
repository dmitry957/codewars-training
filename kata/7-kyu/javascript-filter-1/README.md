# Javascript filter - 1

## Description
While developing a website, you detect that some of the members have troubles logging in. Searching through the code you find that all logins ending with a "_" make problems. So you want to write a function that takes an array of pairs of login-names and e-mails, and outputs an array of all login-name, e-mails-pairs from the login-names that end with "_".

If you have the input-array:

```python
[ [ "foo", "foo@foo.com" ], [ "bar_", "bar@bar.com" ] ]
```
it should output

```python
[ [ "bar_", "bar@bar.com" ] ]
```
You have to use the filter-method which returns each element of the array for which the filter-method returns true.

[Python filter() documentation](https://docs.python.org/3/library/functions.html#filter)

---

#Regular Expressions #Fundamentals