__author__ = 'dias'

import math


def parse_binary(str_num):
    if not is_valid(str_num):
        raise ValueError()

    return int(sum(int(x) * math.pow(2, i) for i, x in enumerate(reversed(str_num))))


def is_valid(num):
    for x in num:
        if x != '1' and x != '0':
            return False
    return True


print(parse_binary('10011'))
