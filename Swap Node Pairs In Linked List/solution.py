from preloaded import Node

def swap_pairs(head):
    if not head or not head.next:
        return head

    first = head
    second = head.next
    first.next = second.next
    second.next = first
    head = second

    cur_nod = first

    while cur_nod.next and cur_nod.next.next:
        first = cur_nod.next
        second = cur_nod.next.next
        first.next = second.next
        second.next = first
        cur_nod.next = second
        cur_nod = first


    return head
