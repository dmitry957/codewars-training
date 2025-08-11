class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def build_tree(inorder, postorder):
    if not inorder or not postorder:
        return None
    
    index_map = {value: idx for idx, value in enumerate(inorder)}
    post_index = [len(postorder) - 1]
    def build(left, right):
        if left > right:
            return None
        
        root_value = postorder[post_index[0]]
        post_index[0] -= 1
        root = TreeNode(root_value)
        mid = index_map[root_value]
        root.right = build(mid + 1, right)
        root.left = build(left, mid - 1)
        return root
    return build(0, len(inorder) - 1)