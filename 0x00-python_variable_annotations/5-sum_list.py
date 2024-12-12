#!/usr/bin/env python3
""" complext annotation example """


def sum_list(input_list) -> float:
    """ returns a float sum in list """

    from functools import reduce
    return float(reduce(lambda x, y: x + y, input_list))
