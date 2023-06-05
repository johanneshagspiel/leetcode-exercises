from typing import List
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = columns = 9

        rows_set_list = [set() for row in range(rows)]
        columns_set_list = [set() for column in range(columns)]
        box_set_list = [set() for column in range(columns)]

        for row in range(rows):
            for column in range(columns):
                current_value = board[row][column]

                if current_value != ".":
                    current_box = (row // 3) * 3 + (column // 3)

                    rows_set_list[row].add(current_value)
                    columns_set_list[column].add(current_value)
                    box_set_list[current_box].add(current_value)

        back
