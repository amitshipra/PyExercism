__author__ = 'agupta'

# Compute all pythagorean triplets (a,b,c) with min <= a,b,c <= max
def triplets_in_range(_min, _max):
    triplets = {a + b + c: (a, b, c) for a in range(_min, _max + 1) for b in range(_min, _max + 1) for c in
                range(_min, _max + 1) if is_triplet(a, b, c)}

    return [triplet for _, triplet in triplets.items()]


def is_triplet(a, b, c):
    return (a * a + b * b) == c * c

def primitive_triplets(b):
    pass


print(triplets_in_range(1, 10))


