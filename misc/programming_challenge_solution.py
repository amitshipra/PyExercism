__author__ = 'dias'

# Problem 1
def numerology(num):
    if len(str(num)) == 1:
        return num
    else:
        return numerology(sum([int(x) for x in str(num)]))


print(numerology(651978))


# Problem 2:
# each of x,y,z are assumed to be tuples (a,b)
import math


def middle_length(x, y, z):
    def side_length(a, b):
        return math.sqrt(pow(b[0] - a[0], 2) + pow(b[1] - a[1], 2))

    side1 = side_length(x, y)
    side2 = side_length(y, z)
    side3 = side_length(z, x)

    return side1 + side2 + side3 - max(side1, side2, side3) - min(side1, side2, side3)


print(middle_length((0.8, 1), (0, 1), (0, 1.6)))

# Problem 5
import itertools


def largest_num(arr):
    combinations = list()
    for lst in itertools.permutations(arr):
        base = ''
        for num in lst:
            base += str(num)
        combinations.append(int(base))
    return max(combinations)


print(largest_num([50, 2, 1, 9]))


# Problem 3
BASE_AMOUNTS = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
                10: 'Ten',
                11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
                17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen',
                20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty',
                90: 'Ninety', 1000: 'One Thousand'}


def amount_in_words(num):
    if num not in range(1, 1001):
        return 'Undefined'
    if num in BASE_AMOUNTS:
        return BASE_AMOUNTS[num]

    def two_digit_str(n):
        if n in BASE_AMOUNTS:
            return BASE_AMOUNTS[n]
        last_digit = n % 10
        first_digit = (n - last_digit) / 10
        return BASE_AMOUNTS[first_digit * 10] + ' ' + BASE_AMOUNTS[last_digit]

    if num < 100:
        return two_digit_str(num)
    else:
        last_two_digit = num % 100
        hundred_digit = (num - last_two_digit) / 100
        if last_two_digit == 0:
            return BASE_AMOUNTS[hundred_digit] + ' hundred '
        else:
            return BASE_AMOUNTS[hundred_digit] + ' hundred ' + two_digit_str(last_two_digit)

    return num


print(amount_in_words(990))
