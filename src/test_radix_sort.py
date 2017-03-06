"""Test the radix sort implementation."""
from random import randint
from radix_sort import radix_sort

def test_radix_sort_empty_list():
    """Test radix sort on empty list."""
    assert radix_sort([]) == []


def test_radix_sort_list_of_one():
    """Test insertion sort returns list of one item."""
    assert radix_sort([99]) == [99]


def test_radix_sort_some_list():
    """Test on the list of numbers I used in iPython."""
    assert radix_sort([22, 11, 4423, 2324, 45436, 254563, 13, 122, 545, 0, 1, 5453, 90]) \
        == [0, 1, 11, 13, 22, 90, 122, 545, 2324, 4423, 5453, 45436, 254563]


def test_radix_sort_on_randomized_list():
    """Test on random list of random length."""
    from radix_sort import radix_sort
    test_list = [randint(0, 100) for i in range(randint(10, 100))]
    assert radix_sort(test_list) == sorted(test_list)
