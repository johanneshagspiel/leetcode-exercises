import collections
from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:


        def _sort_diagonal(start_column, start_row):

            diagonal = []

            column = start_column
            row = start_row

            while row >= 0 and column >= 0:
                diagonal.append(mat[column][row])

                column -= 1
                row -= 1

            sorted_diagonal = _count_sort(diagonal)

            column = start_column
            row = start_row

            while row >= 0 and column >= 0:
                mat[column][row] = sorted_diagonal.pop()

                column -= 1
                row -= 1


        def _count_sort(diagonal):

            number_count = collections.Counter(diagonal)

            minimum = 1
            maximum = 100

            sorted_diagonal = []

            for number in range(minimum, maximum + 1):
                sorted_diagonal.extend([number] * number_count[number])

            return sorted_diagonal


        columns = len(mat)
        rows = len(mat[0])

        for column in range(columns):
            _sort_diagonal(column, rows - 1)

        for row in range(rows -2, -1, -1):
            _sort_diagonal(columns - 1, row)

        return mat

