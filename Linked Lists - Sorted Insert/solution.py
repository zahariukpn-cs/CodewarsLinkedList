""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
    if not head:
        return Node(data)
    current_node = head
    prev_node = head
    if data < head.data:
                head = Node(data)
                head.next = current_node
                return head
    while current_node:
            if data < current_node.data:
                prev_node.next = Node(data)
                prev_node.next.next = current_node
                return head
            prev_node = current_node
            current_node = current_node.next
    prev_node.next = Node(data)
    return head

    # Make sure to return the head of the list.
