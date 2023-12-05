#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:

# (C) 2023 Qusai alismat, Sudan
# email igozeco120@gmail.com
# -----------------------------------------------------------


def replace_in_list(my_list, idx, element):
    """Replaces an element of a list at a specific position
        my_list: a list
    """

    # Check for negative and out of range index
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list

