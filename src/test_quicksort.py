from quicksort import quicksort

import pytest


ASSERTIONS = [
    ([34, 45, 20, 1, 3, 5, 65, 100],
     [1, 3, 5, 20, 34, 45, 65, 100]),
    ([34, 45, 76, 1, 3, 5, 6, 8, 3, 98, 654, 23, 0, 3, 100],
     [0, 1, 3, 3, 3, 5, 6, 8, 23, 34, 45, 76, 98, 100, 654]),
    ([54, 65, 34, 7, 4, 2, 5, 7876, 34, 90, 17, 32, 7, 5, 23, 83],
     [2, 4, 5, 5, 7, 7, 17, 23, 32, 34, 34, 54, 65, 83, 90, 7876]),
    ([0, 4, 6, 13, 0, 6, 4, 0, 6, 7, 3],
     [0, 0, 0, 3, 4, 4, 6, 6, 6, 7, 13]),
    ([0, 4, 6, 13],
     [0, 4, 6, 13]),
    ([4, 13, 0, 6],
     [0, 4, 6, 13]),
]


@pytest.mark.parametrize("unsorted_list, sorted_list", ASSERTIONS)
def test_quicksort(unsorted_list, sorted_list):
    """Test for quicksort."""
    assert quicksort(unsorted_list) == sorted_list
