"""Implementation of merge sort.

This version recusrively divides the input list into sublists small enough
to be sorted on their own, then merges them. When run as a script, 
a timeit function runs merge_sort() on a list of 200 random integers 
three times, and returns the run time for each.


Methods include:
merge_sort(a_list): Recursively divides list at midpoint, more or less.
merge(list1, list2): A helper function to do the comparisons between values.
"""


def merge_sort(a_list):
    """Divide, conquer to sort list."""
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