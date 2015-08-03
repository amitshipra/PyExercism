__author__ = 'dias'

import random
import time


def solution(X, A):
    def is_equal(idx):
        left, right = A[:idx], A[idx:]
        left_count = sum(1 for e in left if e == X)
        right_count = sum(1 for e in right if e != X)

        if left_count == right_count:
            if len(A) <= 20:
                print left, ':', right
            return idx
        return None

    start = time.time()
    for idx in range(1, len(A)):
        if is_equal(idx) is not None:
            elapsed = time.time() - start
            print('Solution Found. Time Taken for Array length [%d] is %d ', len(A), elapsed)
            return idx

    elapsed = time.time() - start
    print('No Solution Found. Time Taken for Array length [%d] is %d ', len(A), elapsed)

    return -1


array = list()
N = 10
for _ in range(1, N):
    array.append(random.randint(1, 5))

print solution(1, array)
