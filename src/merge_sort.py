"""Merge sort implementation."""


def merge_sort(a_list):
    """Divide, conquer to sort list."""
    # import pdb; pdb.set_trace()
    if len(a_list) <= 1:
        return a_list
    midpoint = (len(a_list) // 2)
    first_half = a_list[:midpoint]
    second_half = a_list[midpoint:]
    first_half = merge_sort(first_half)
    second_half = merge_sort(second_half)
    return merge(first_half, second_half)


def merge(list1, list2):
    """The helper function to do the comparisons."""
    # import pdb; pdb.set_trace()
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


if __name__ == "__main__":

    import timeit
    import random

    def build_random_list():
        """Build a random list to sort."""
        rand_list = [random.randint(0, 1000) for i in range(200)]
        return rand_list

    lst = build_random_list()

    print(timeit.repeat(stmt='merge_sort(lst)',
                        setup='from __main__ import merge_sort, lst, random', repeat=3,
                        number=1000
                        )
          )

    # print(timeit.repeat(stmt='g.breadth_first_traversal(random.choice(list(g.node_dict.keys())))',
    #                     setup='from __main__ import SimpleGraph, g, random', repeat=3,
    #                     number=1000
    #                     )
    #       )
