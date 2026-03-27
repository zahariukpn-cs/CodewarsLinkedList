class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if not head or not head.next:
        raise ValueError
    first_head = head
    second_head = head.next

    first_cur = first_head
    second_cur = second_head

    while second_cur and second_cur.next:
        first_cur.next = second_cur.next
        second_cur.next = second_cur.next.next

        first_cur = first_cur.next
        second_cur = second_cur.next

    first_cur.next = None

    return Context(first_head, second_head)
