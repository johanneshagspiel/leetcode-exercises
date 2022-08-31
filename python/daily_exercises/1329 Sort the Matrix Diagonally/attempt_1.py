from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:

        columns = len(mat)
        rows = len(mat[0])

        row_dic = {}
        start_row = rows - 1

        for column in range(columns):
            current_diagonal = []
            start_column = column

            current_row = start_row
            current_column = start_column

            while current_column >= 0 and current_row >= 0:
                current_cell = mat[current_column][current_row]
                current_diagonal.append(current_cell)

                current_column -= 1
                current_row -= 1

            row_dic[(start_column, start_row)] = current_diagonal


        start_column = columns - 1

        for row in range(rows-2, -1, -1):
            current_diagonal = []
            start_row = row

            current_row = start_row
            current_column = start_column

            while current_column >= 0 and current_row >= 0:
                current_cell = mat[current_column][current_row]
                current_diagonal.append(current_cell)

                current_column -= 1
                current_row -= 1

            row_dic[(start_column, start_row)] = current_diagonal


        sorted_row_dic = {}

        for key, value_list in row_dic.items():
            sorted_value_list = sorted(value_list)
            sorted_row_dic[key] = sorted_value_list


        start_row = rows - 1

        for column in range(columns):
            start_column = column

            current_row = start_row
            current_column = start_column

            sorted_diagonal = sorted_row_dic.pop((start_column, start_row))

            while current_column >= 0 and current_row >= 0:
                mat[current_column][current_row] = sorted_diagonal.pop()

                current_column -= 1
                current_row -= 1


        start_column = columns - 1

        for row in range(rows-2, -1, -1):
            start_row = row

            current_row = start_row
            current_column = start_column

            sorted_diagonal = sorted_row_dic.pop((start_column, start_row))

            while current_column >= 0 and current_row >= 0:
                mat[current_column][current_row] = sorted_diagonal.pop()

                current_column -= 1
                current_row -= 1

        return mat