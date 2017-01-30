"""Insertion sort."""

def insertion_sort(some_list):
    """some doc."""
    if not hasattr(some_list, "__iter__"):
        raise(TypeError)
    idx = 0
    while idx < len(some_list) - 1:
        if some_list[idx] > some_list[idx + 1]:
            some_list[idx], some_list[idx + 1] = some_list[idx + 1], some_list[idx]
            for i in some_list[:idx:-1]:
                import pdb; pdb.set_trace()
                if some_list[idx] < i:
                    some_list[idx], i = i, some_list[idx]
        idx += 1
    return some_list
