__author__ = 'dias'


def solution(X, A):
    def is_equal(idx):
        left, right = A[:idx], A[idx:]
        left_count = sum(1 for e in left if e == X)
        right_count = sum(1 for e in right if e != X)

        if left_count == right_count:
            print left, ':', right
            return idx
        return -1

    # This finds all the indexes. We can abort the search with first one if performance is an issue.
    for idx in range(1, len(A)):
        if is_equal(idx) != -1:
            return idx

    return -1


print solution(5, [5, 5, 3, 2, 5, 6, 7, 8])
