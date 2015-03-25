__author__ = 'agupt15'


def sieve(limit):
    # create the list
    num_map = {n: True for n in range(limit + 1) if n >= 2}

    def mark_divisiblity(divisor):
        if divisor >= limit / 2:
            return None

        for n in range(limit + 1):
            if n <= divisor:
                continue
            elif n % divisor == 0:
                num_map[n] = False

        divisor += 1
        mark_divisiblity(divisor)

    mark_divisiblity(2)

    return [n for n in num_map if num_map[n] is True]
