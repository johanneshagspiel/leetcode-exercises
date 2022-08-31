from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:

        def sort_diagonal(start_column, start_row):

            diagonal = []

            column = start_column
            row = start_row

            while column >=0 and row >= 0:
                diagonal.append(mat[column][row])

                row -= 1
                column -= 1

            diagonal.sort()

            column = start_column
            row = start_row

            while column >=0 and row >= 0:
                mat[column][row] = diagonal.pop()
                row -= 1
                column -= 1

        columns = len(mat)
        rows = len(mat[0])

        for column in range(columns):
            sort_diagonal(column, rows - 1)

        for row in range(rows-2, -1, -1):
            sort_diagonal(columns - 1, row)

        return mat
