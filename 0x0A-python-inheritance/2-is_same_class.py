#!/usr/bin/python3
def is_same_class(obj, a_class):
    """ This function returns True or False if obj is a type of a_class
    Args:
        obj: object
        a_class: class type
    Returns:
        True if obj is exactly an instance of a_class
        False, otherwise
    """
    return (type(obj) is a_class)
