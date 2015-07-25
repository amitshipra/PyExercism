__author__ = 'dias'


def saddle_points(matrix):
    saddles = []
    for row_idx, row in enumerate(matrix):
        for col_idx, col in enumerate(row):
            #            print('Element at (' + str(row_idx) + ',' + str(col_idx) + ') : ' + str(matrix[row_idx][col_idx]))
            if is_saddle(row_idx, col_idx, matrix):
                saddles.append((row_idx, col_idx))
    return set(saddles)


def is_saddle(row_idx, col_idx, matrix):
    return max(get_row(matrix, row_idx)) == matrix[row_idx][col_idx] and min(get_column(matrix, col_idx)) == \
                                                                         matrix[row_idx][col_idx]


def get_row(matrix, idx):
    return matrix[idx]


def get_column(matrix, idx):
    column = []
    for _, row in enumerate(matrix):
        for c_i, element in enumerate(row):
            if c_i == idx:
                column.append(element)

    return column

    return matrix[idx]

print(saddle_points([[2, 1], [1, 2]]))
