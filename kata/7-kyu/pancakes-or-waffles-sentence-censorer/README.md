# Pancakes or Waffles [Sentence Censorer]

[Codewars Kata Link](https://www.codewars.com/kata/674d4d8e3520c1e84eacf11e/python)

## Description

The owner of a certain chatbox app has came under fire recently for a drama regarding the age old debate of pancakes or waffles. Because of this, he came to you in order to hide any words regarding pancakes.

The following words are the words that he is looking to censor by replacing it with an equal amount of astricks (`*`):

- pancakes
- flapjacks
- slapjacks
- hotcakes

In conjunction to that, the following words shall be highlighted with a double astricks (`**`):

- waffles
- crepes
- blintzes

Finally, as long as there is no mention of a waffle relating word in the sentence, also censor the following word unless, there is a waffle relating word then highlight it:

- syrup
- honey
- jam
- butter
- chocolate
- margarine

### Examples

```python
print(censor("I like waffles with chocolate")) --> "I like **waffles** with **chocolate**"

print(censor("I like pancakes with syrup")) --> "I like ******* with *****"

print(censor("The debate between pancakes and waffles is as sweet as honey")) --> "The debate between ******** and **waffles** is as sweet as **honey**"
```