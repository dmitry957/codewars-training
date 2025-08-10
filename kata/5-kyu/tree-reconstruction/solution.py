def reconstruct_tree(in_order, pre_order):
    if not in_order:
        return []
    root = pre_order[0]
    root_index = in_order.index(root)
    left_in = in_order[:root_index]
    right_in = in_order[root_index + 1:]
    left_pre = pre_order[1:1 + len(left_in)]
    right_pre = pre_order[1 + len(left_in):]
    return [root, reconstruct_tree(left_in, left_pre), reconstruct_tree(right_in, right_pre)]