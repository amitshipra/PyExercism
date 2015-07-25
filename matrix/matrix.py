__author__ = 'dias'


class Matrix:
    def __init__(self, input):
        self._input = input
        self._rows = [row for row in self._input.split('\n')]
        self._matrix = [element.split(' ') for element in self._rows]
        self.rows = []
        self.columns = []
        for row in self._matrix:
            self.rows.append([int(x) for x in row])

        col_num = len(self.rows[0])
        for i in range(col_num):
            col = []
            self.columns.append(col)
            for row in self.rows:
                col.append(row[i])
