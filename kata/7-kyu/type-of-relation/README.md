# Type Of Relation

[Codewars Kata Link](https://www.codewars.com/kata/64915dc9d40f96004319379a/python)

## Description

Given two sets of integer numbers (domain and codomain), and a list of relationships `(x, y)` (also integers), determine if they represent a function and its type:

### 1. Not a function
If there is at least one element in the domain set that is related to more than one element in the codomain set.

**Example:**
```python
domain = {10, 20, 30, 40, 50}
codomain = {20, 30, 40, 50}
relations = {(10, 20),(10, 50),(20, 30),(30, 40),(40, 50),(50, 20)}
output = "It is not a function"
```
(this is because the element 10 in the domain is related to more than one element in the codomain, therefore, it does not fulfill the uniqueness criterion).

### 2. Function
Each and every element in the domain set is related to an element in the codomain set. They are classified as:

#### A. Injective
Every element in the codomain set is related to at most one element in the domain set. In other words, there are no two distinct elements in the domain set that have the same image in the codomain set.

**Example:**
```python
domain = {1, 2}
codomain = {20, 30, 40}
relations = {(1, 20),(2, 30)}
output = "Injective"
```
(because each element in the codomain is related to zero or at most one element in the domain).

#### B. Surjective
All elements in the codomain set are related to at least one element in the domain set. In other words, there are no elements in the codomain set that do not have a preimage in the domain set.

**Example:**
```python
domain = {1, 2, 3, 4, 5}
codomain = {20, 30, 40, 50}
relations = {(1, 20),(2, 30),(3, 40),(4, 50),(5, 40)}
output = "Surjective"
```
(because all elements in the codomain are related to at least one element in the domain, element 40 has more than one relation in the domain).

#### C. Bijective
Every element in the domain set is related to a unique element in the codomain set, and vice versa. Each element in the codomain set has a unique preimage in the domain set, and each element in the domain set has a unique image in the codomain set.

In other words, a function is bijective when it is injective and surjective at the same time.

**Example:**
```python
domain = {2, 3, 4}
codomain = {2, 3, 4}
relations = {(3, 4),(2, 3),(4, 2)}
output = "Bijective" 
```
(because each element in the codomain is related to exactly one element in the domain).

#### D. General
There are elements in the domain set that are related to at least one element in the codomain set, but there may be elements in the codomain set that are not related to any element in the domain set.

**Example:**
```python
domain = {1, 2, 3}
codomain = {2, 3, 4}
relations = {(1, 4),(2, 4),(3, 4)}
output = "General function"
```
(all elements in the domain are related to at least one element in the codomain, although some elements in the codomain are not related to any element in the domain).

**Note:** All the first elements in the relations belong to the domain set, and all the second elements belong to the codomain set.

---

#Mathematics #Set Theory