__author__ = 'dias'

import math


def parse_binary_to_decimal(arr):
    if not is_valid(arr):
        raise ValueError('Invalid Binary rep')

    return sum(x * math.pow(2, i) for i, x in enumerate(arr))

def parse_binary_to_decimal_negative(arr):
    if not is_valid(arr):
        raise ValueError('Invalid Binary rep')

    return sum(x * math.pow(-2, i) for i, x in enumerate(arr))


def is_valid(num):
    for x in num:
        if x != 1 and x != 0:
            return False
    return True


print('Positive: ' + parse_binary_to_decimal([1, 0, 0, 1, 1, 1]))
