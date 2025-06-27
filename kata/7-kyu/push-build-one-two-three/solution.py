class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def push(head, data):
    if head is None:
        head = Node(data)
        head.next = None
    else:
        new_node = Node(data)
        new_node.next = head
        head = new_node
    return head

def build_one_two_three():
    return push(push(push(None, 3), 2), 1)
