#!/usr/bin/python3


def max_integer(my_list=[]):
    """finds biggest integer of a list"""
    if len(my_list) == 0:
        return (None)

    biggest_int = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > big:
            biggest_int = my_list[i]

    return (biggest_int)
