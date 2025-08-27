class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def linked_list_from_string(s):
    nodes = [int(n) for n in s.split(' -> ')[:-1]]
    head = None
    for n in reversed(nodes):
        head = Node(n, head)
    return head