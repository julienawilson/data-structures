"""Implementation of insertion sort.

Sort is done in-place iterating through the list, reordering the list
from index 0 up.
"""

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

if __name__ == "__main__":

    import timeit
    import random

    def build_random_list():
        """Build a random list to sort."""
        rand_list = [random.randint(0, 1000) for i in range(200)]
        return rand_list

    lst = build_random_list()

    print(timeit.repeat(stmt='insertion_sort(lst)',
                        setup='from __main__ import insertion_sort, lst, random', repeat=3,
                        number=1000
                        )
          )
