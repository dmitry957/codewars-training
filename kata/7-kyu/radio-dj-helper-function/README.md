# Radio DJ Helper Function

[View on Codewars](https://www.codewars.com/kata/561bbcb0fbbfb0f5010000ee/python)

---

## The Problem
James is a DJ at a local radio station. As it's getting to the top of the hour, he needs to find a song to play that will be short enough to fit in before the news block. He's got a database of songs that he'd like you to help him filter in order to do that.

---

## What To Do
Create `longestPossible` (`longest_possible` in Python and Ruby) helper function that takes 1 integer argument which is the maximum length of a song in seconds.

`songs` is an array of objects which are formatted as follows:

```python
{'artist': 'Artist', 'title': 'Title String', 'playback': '04:30'}
```
You can expect the `playback` value to be formatted exactly like above.

Output should be the title of the longest song from the database that matches the criteria of not being longer than the specified time. If there are no songs matching the criteria in the database, return `False`.

---

**Tags:** `#Sorting` `#Filtering` `#Algorithms`