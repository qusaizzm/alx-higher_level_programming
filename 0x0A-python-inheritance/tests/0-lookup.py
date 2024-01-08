#!/usr/bin/python3
'''Module for lookup method.'''


def get_object_attributes(obj):
    '''Looks up object attributes and methods.

    Args:
        obj (object): The object to list.

    Returns:
        list: The list of attributes.
    '''
    return dir(obj)
