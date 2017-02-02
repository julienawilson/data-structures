"""Implementation of a Radix Sort."""
import math


def radix_sort(iter):
    """Sort a list using the radix sort method."""
    number_holder = {}
    for number in iter:
        number_holder[number % 10] = number
    return number_holder




def rounddown(x, mag):
    return int(math.floor(x / mag)) * mag
