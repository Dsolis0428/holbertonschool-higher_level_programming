#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """prints interger of list in reverse order"""
    if my_list:
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))