class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head, prev=None):
    if not head:
        return None
    if not head.next:
        head.next = prev
        return head
    nxt_nod = head.next
    head.next = prev
    return reverse(nxt_nod, head)
