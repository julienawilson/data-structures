"""Implementation of quicksort."""


def quicksort(array):
    """Divide, sort, conquer, the quicksort way."""
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == "__main__":

    import timeit
    import random

    def build_random_list():
        """Build a random list to sort."""
        rand_list = [random.randint(0, 10000) for i in range(200)]
        return rand_list

    lst = build_random_list()

    print(timeit.repeat(stmt='quicksort(lst)',
                        setup='from __main__ import quicksort, lst, random', repeat=3,
                        number=10000
                        )
          )
