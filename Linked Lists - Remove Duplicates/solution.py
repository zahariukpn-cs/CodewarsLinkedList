class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if not head:
        return None
    cur_nod = head
    while cur_nod.next:
        if cur_nod.data == cur_nod.next.data:
            cur_nod.next = cur_nod.next.next
        else:
            cur_nod = cur_nod.next
    return head
