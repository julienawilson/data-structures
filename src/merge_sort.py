"""Merge sort implementation."""


def merge_sort(a_list):
    """Divide, conquer to sort list."""
    import pdb; pdb.set_trace()
    if len(a_list) <= 1:
        return a_list
    midpoint = (len(a_list) // 2)
    first_half = a_list[:midpoint]
    second_half = a_list[midpoint:]
    merge_sort(first_half)
    merge_sort(second_half)
    return merge(first_half, second_half)


def merge(list1, list2):
    """The helper function to do the comparisons."""
    result = []
    while list1 and list2:
        if list1[0] <= list2[0]:
            result.append(list1.pop(0))
        else:
            result.append(list2.pop(0))
    if list1:
        result += list1
    if list2:
        result += list2
    return result
