from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    res_lst = list_repr.split(' -> ')
    node = None
    res_lst = res_lst[:-1]
    for el in reversed(res_lst):
        node = Node(int(el), node)
    return node
