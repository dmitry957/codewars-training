def list_to_array(node):
    result = [node.value]
    while node.next != None:
        result.append(node.next.value)
        node = node.next
    return result