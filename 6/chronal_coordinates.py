"""https://adventofcode.com/2018/day/6"""


class Matrix:
    """Homebrewed matrix class"""
    def __init__(self, x_len: int = 0, y_len: int = 0):
        if not x_len and y_len:
            # Empty matrix initializer
            self._matrix = [[]]
        elif x_len == 0:
            raise ValueError('A matrix cannot have a column without a row')
        elif y_len == 0:
            raise ValueError('A matrix cannot have a row without a column')
        else:
            self._matrix = [[] * x_len] * y_len

    def __repr__(self):
        out = ''
        for row in self._matrix:
            out += f'{str(row)}\n'
        return out

    @property
    def rows(self):
        return len(self._matrix)

    @property
    def columns(self):
        return len(self._matrix[0])

    @property
    def size(self):
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError

    def transpose(self):
        raise NotImplementedError

    def append_row(self, row_num):
        raise NotImplementedError

    def insert_row(self, row_num: int):
        raise NotImplementedError

    def remove_row(self, row_num: int):
        raise NotImplementedError

    def append_column(self, col_num: int):
        self.insert_column(self.columns + 1)

    def insert_column(self, col_num: int):
        if col_num > self.columns:
            raise IndexError

    def remove_column(self, col_num: int):
        raise NotImplementedError

    def index(self, row: int, col: int):
        # TODO: This might not be needed as we can access an x,y pair in a list of lists directly
        #  some_list_of_lists[1][4]
        raise NotImplementedError


def taxicab_distance(source: tuple, sink: tuple) -> int:
    assert len(source) == len(sink)

    distance = 0
    for i, source_coord in enumerate(source):
        distance += abs(source_coord - sink[i])
    return distance


# Get input as a list of coordinate pairs(tuple of integers)
test_input = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9""".split('\n')
test_input = [tuple(int(coord) for coord in coords.split(','))
              for coords in test_input]

with open('input.txt') as indata:
    data = [tuple(int(coord) for coord in coords.split(','))
            for coords in indata.readlines()]

if __name__ == '__main__':
    m = Matrix(3,3)
    print(m)
    m.append_column(1)