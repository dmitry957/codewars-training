# Find Array - 7 kyu

## Kata Description

You are given two arrays `arr1` and `arr2`, where `arr2` contains indices. Your task is to return a new array containing elements from `arr1` at the indices specified in `arr2`.

## Solution

The solution uses a list comprehension to extract elements from `arr1` at the indices specified in `arr2`, with bounds checking to ensure indices are valid.

```python
def find_array(arr1, arr2):
    return [arr1[i] for i in arr2 if 0 <= i < len(arr1)]
```

## Approach

1. **List Comprehension**: Uses Python's list comprehension for concise and readable code
2. **Bounds Checking**: The condition `0 <= i < len(arr1)` ensures we only access valid indices
3. **Element Extraction**: For each valid index `i` in `arr2`, extracts `arr1[i]`

## Examples

```python
find_array(['a', 'a', 'a', 'a', 'a'], [2, 4])  # Returns: ['a', 'a']
find_array([0, 1, 5, 2, 1, 8, 9, 1, 5], [1, 4, 7])  # Returns: [1, 1, 1]
find_array([1, 2, 3, 4, 5], [0])  # Returns: [1]
find_array([1, 2, 3, 4, 5], [4, 2, 0])  # Returns: [5, 3, 1]
```

## Time Complexity

- **Time**: O(n) where n is the length of `arr2`
- **Space**: O(n) for the result array

## Edge Cases Handled

- Empty arrays
- Invalid indices (out of bounds)
- Duplicate indices
- Indices in any order 