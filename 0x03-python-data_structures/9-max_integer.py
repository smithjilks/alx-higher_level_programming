#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)

    if length == 0:
        return (None)

    max_int = my_list[0]
    for i in range(length - 1):
        if max_int < my_list[i + 1]:
            max_int = my_list[i + 1]

    return (max_int)
