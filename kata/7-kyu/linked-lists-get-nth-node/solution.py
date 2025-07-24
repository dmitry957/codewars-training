class Node(object):
     """Node class for reference"""
     def __init__(self, data, next=None):
         self.data = data
         self.next = next
    
def get_nth(node, index):
    if node is None:
        raise ValueError('None linked list should throw error.')
    
    return node if index == 0 else get_nth(node.next, index - 1)
    # Your code goes here.