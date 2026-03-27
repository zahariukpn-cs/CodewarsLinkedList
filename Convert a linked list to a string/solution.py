def stringify(node):
    res = []
    while node:
        current = node
        node = current.next
        res.append(str(current.data))
    res.append('None')
    return ' -> '.join(res)
