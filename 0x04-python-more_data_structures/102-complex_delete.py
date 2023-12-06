#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    # Use dictionary comprehension to create a new dictionary without the specified keys
    updated_dict = {
            key:
            val for key, 
            val in a_dictionary.items() 
            if val != value
            }
    return updated_dict
