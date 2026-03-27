class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    counter = 0
    if not node:
        return InvalidArgumentException
    while node:
        if counter == index:
            return node
        counter += 1
        node = node.next
    return InvalidArgumentException
