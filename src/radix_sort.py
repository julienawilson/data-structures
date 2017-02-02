"""Implementation of a Radix Sort."""
import math


def radix_sort(iter):
    """Sort a list using the radix sort method."""
    number_holder = {}
    flat_list = iter
    magnitude = 1
    loop = True
    while loop:
        number_holder = {}
        loop = False
        for number in flat_list:
            the_key = grab_digit(number, magnitude)
            if the_key > 0:
                loop = True
            number_holder.setdefault(the_key, [])
            number_holder[the_key].append(number)
        flat_list = []
        for number in sorted(number_holder.keys()):
            flat_list += number_holder[number]
        magnitude *= 10
    return flat_list


def grab_digit(x, mag):
    round_down = int(math.floor(x / mag))
    digit = round_down % 10
    return digit