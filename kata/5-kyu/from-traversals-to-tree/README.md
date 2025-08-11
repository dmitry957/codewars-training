# From Traversals to Tree

[Codewars Link](https://www.codewars.com/kata/651478c7ba373c338a173de6/python)

## Description

### Finding a Binary Tree from Traversals

Reconstruct a binary tree from its in-order and post-order traversals. A binary tree is a tree where each node has either 0, 1 or 2 children. Such a tree is usually represented recursively using a class where each node has a value and left and right subtrees (either of which can be None or a similar empty value).

```python
class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
```

For example,

```python
TreeNode(1, TreeNode(2, TreeNode(4), None), TreeNode(3, TreeNode(5, None, None), TreeNode(6, None, None)))
```

represents the tree below.

Trailing Nones can be omitted, as in `TreeNode(4)`.

```
      1
     / \
    2   3
   /   / \
  4   5   6
```

### Traversals

A tree can be traversed in various ways. The in-order traversal visits the left child of each node, then the node itself, then its right child. For example, the in-order traversal of the tree above is `4 2 1 5 3 6`.

Different trees can have the same in-order traversal. For example, the in-order traversal of the tree below is also `4 2 1 5 3 6`.

```
      3
     / \
    1   6
   / \  
  2   5  
 /
4
```

The post-order traversal visits the left child first, then the right child, then the node itself. For example, the post-order traversal of the first tree is `4 2 5 6 3 1`, while the post-order traversal of the second tree is `4 2 5 1 6 3`. Different trees can have the same post-order traversal.

Although neither the in-order traversal nor the post-order traversal identify the tree, the combination of the two does.

## Task

Reconstruct a tree from its in-order and post-order traversals.

- **Input:** Two lists of integers, the first containing the in-order traversal and the second the post-order traversal of a particular tree. Each list will have no duplicate values, so each node is identifiable.
- **Output:** Return the tree whose in-order and post-order traversals match the given values. Subtrees that are None can be omitted or included.

## Examples

```python
build_tree([4, 2, 1, 5, 3, 6], [4, 2, 5, 6, 3, 1])
# should return TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5), TreeNode(6))) or an equivalent representation of the first tree above.

build_tree([4, 2, 1, 5, 3, 6], [4, 2, 5, 1, 6, 3])
# should return TreeNode(3, TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(5)), TreeNode(6)), the second tree above.
```

## Random Tests

There are 2 types of random tests:

- 100 random trees containing from 0 to 15 nodes.
- Five random trees of 150,000 nodes.

## Other Thoughts

There is also a pre-order traversal: Visit the node before visiting its left child and then its right child. To reconstruct a tree from its in-order and pre-order traversals, see Tree Reconstruction. Can a tree be reconstructed from its pre-order and post-order traversals?

Other kata related to binary tree traversals include Perfect Binary Tree Traversal: BFS to DFS, Binary Tree Traversal, and Binary Tree Serpentine Traversal.

#Trees #Recursion #Performance