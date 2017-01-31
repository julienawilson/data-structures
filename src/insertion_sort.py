"""Insertion sort."""

def insertion_sort(some_list):
    """It sorts."""
    if not hasattr(some_list, "__iter__"):
        raise(TypeError)
    idx = 0
    while idx < len(some_list) - 1:
        if some_list[idx] > some_list[idx + 1]:
            some_list[idx], some_list[idx + 1] = some_list[idx + 1], some_list[idx]
            bw_list = some_list[:idx][::-1]
            bw_idx = idx
            for i in range(len(bw_list)):
                # import pdb; pdb.set_trace()
                if some_list[bw_idx] < bw_list[i]:
                    some_list[bw_idx], bw_list[i] = bw_list[i], some_list[bw_idx]
                bw_idx -= 1
        idx += 1
    return some_list
