# Tree Reconstruction

[Codewars Link](https://www.codewars.com/kata/52f56c2be248dfbdc6000f87/python)

Given two traversals of a binary tree, in-order and pre-order, reconstruct the tree.

Background: [Tree traversal - In-order](http://en.wikipedia.org/wiki/Tree_traversal#In-order)

## Example

```
# this is the tree to reconstruct:
#        4
#       / \
#      /   \
#     2     6
#    / \   /
#   1   3 5

in_order  = [1,2,3,4,5,6]
pre_order = [4,2,1,3,6,5]

reconstruct_tree(in_order, pre_order) => [ 4
                                         , [ 2
                                           , [ 1 , [], [] ]
                                           , [ 3 , [], [] ]
                                           ]
                                         , [ 6
                                           , [ 5 , [], [] ]
                                           , []
                                           ]
                                         ]
```

#Algorithms #Trees #Recursion