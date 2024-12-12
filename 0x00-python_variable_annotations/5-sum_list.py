#!/usr/bin/env python3
""" complext annotation example """


from functools import reduce

def sum_list(input_list) -> float:
    """ returns a float sum in list """

    return reduce(lambda x, y: x + y, input_list)
