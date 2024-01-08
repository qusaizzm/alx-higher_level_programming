#!/usr/bin/python3
'''Module for MyList class.'''


class CustomList(list):
    '''Custom MyList class.'''

    def print_sorted(self):
        '''Method for printing a sorted list.'''
        print(sorted(self))
