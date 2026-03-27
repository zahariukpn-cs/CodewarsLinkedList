def loop_size(node):
    if not node or not node.next or not node.next.next:
        return 0
    slow = node.next
    fast = node.next.next
    while slow != fast:
        slow = slow.next
        fast = fast.next.next

        if not slow or not fast:
            return 0

    slow = node
    while slow != fast:
        slow = slow.next
        fast = fast.next

        if not slow or not fast:
            return 0

    counter = 1
    fast = fast.next
    while fast != slow:
        counter += 1
        fast = fast.next

    return counter
