from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left_pointer = 0
        number_rows = len(matrix) - 1
        number_columns = len(matrix[0])
        right_pointer = number_columns + number_rows * number_columns - 1

        while left_pointer <= right_pointer:
            pivot = left_pointer + ((right_pointer - left_pointer) // 2)
            row = pivot // number_columns
            colum = pivot % number_columns

            pivot_value = matrix[row][colum]

            if pivot_value == target:
                return True
            elif pivot_value < target:
                left_pointer = pivot + 1
            else:
                right_pointer = pivot - 1

        return False


