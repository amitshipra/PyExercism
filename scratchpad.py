__author__ = 'dias'


def sort_priority(numbers, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (4, x)

    numbers.sort(key=helper)


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = [2, 3, 5, 7]

sort_priority(numbers, group)
print(numbers)
