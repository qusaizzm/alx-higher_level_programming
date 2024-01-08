#!/usr/bin/python3
'''Module for is_same_class method.'''


def is_instance_of(obj, target_class):
    '''Determines if an object is exactly an instance of a class.'''
    return type(obj) == target_class

