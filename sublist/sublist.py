__author__ = 'agupta'

class EQUAL:
    pass


class UNEQUAL:
    pass


class SUBLIST:
    pass


class SUPERLIST:
    pass


def check_lists(list1, list2):
    if len(list1) == 0 and len(list2) == 0:
        return EQUAL

    if len(list1) == 0 and len(list2) != 0:
        return SUBLIST

    if len(list2) == 0 and len(list1) != 0:
        return SUPERLIST

    def is_equal(l1, l2):
        if len(l1) != len(l2):
            return False

        for x, y in zip(l1, l2):
            if x != y:
                return False
        return True

    if len(list1) == len(list2) and is_equal(list1, list2):
        return EQUAL

    if len(list1) > len(list2):
        long_list, small_list = list1, list2
    else:
        long_list, small_list = list2, list1

    def is_sublist(_small_list, _long_list):
        first_element = _small_list[0]
        if first_element not in _long_list:
            return UNEQUAL

        index_first_element = _long_list.index(first_element)

        sub_list = _long_list[index_first_element:index_first_element + len(_small_list)]
        if is_equal(sub_list, _small_list):
            return EQUAL
        else:
            return is_sublist(_small_list, _long_list[index_first_element + 1:])

    is_sublist = is_sublist(small_list, long_list)
    if is_sublist == EQUAL and is_equal(list1, small_list):
        return SUBLIST
    elif is_sublist == EQUAL and is_equal(list2, small_list):
        return SUPERLIST
    else:
        return UNEQUAL