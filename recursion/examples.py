__author__ = 'agupt15'
# Source: http://www.python-course.eu/python3_recursive_functions.php
#
#
#
#

# ## Example 1
#
# Write a recursive Python function that returns the sum of the first n integers.
###


def rec_add(num):
    if num == 1:
        return 1
    return num + rec_add(num - 1)


print(rec_add(10))


### Exmple 1.1: Add numbers in a list using recursion.

def add_list(lst, total = 0):
    return None


### Example 2
#
# Write a function which implements the Pascal's triangle:
#
#                       1
#                    1    1
#                  1    2    1
#                1    3    3    1
#              1    4    6    4    1
#           1    5    10    10    5    1

def pascal_triangle(row_count):
    return None
