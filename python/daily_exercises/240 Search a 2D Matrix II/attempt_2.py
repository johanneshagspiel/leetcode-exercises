from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n = len(matrix)
        m = len(matrix[0])

        if n <= 2 or m <= 2:

            for i in range(n):
                for j in range(m):
                    if matrix[i][j] == target:
                        return True

            return False


        left = 0
        right = m-1

        row = 0
        column = 0

        row_mode = True

        last_pivot_column = None
        last_pivot_row = None

        pivot_row = None
        pivot_row = None

        while True:

            while left < (right-1):

                pivot = left + ((right - left) // 2)

                if row_mode:
                    pivot_column = pivot
                    pivot_num = matrix[row][pivot]
                    left_num = matrix[row][left]
                    right_num = matrix[row][right]
                else:
                    pivot_row = pivot
                    pivot_num = matrix[pivot][column]
                    left_num = matrix[left][column]
                    right_num = matrix[right][column]

                if left_num == target or right_num == target or pivot_num == target:
                    return True

                elif pivot_num < target:
                    left = pivot

                else:
                    right = pivot


            if row_mode:
                if last_pivot_column == pivot and last_pivot_row == row:
                    return False
                else:
                    last_pivot_column = pivot
            else:
                if last_pivot_column == column and last_pivot_row == pivot:
                    return False
                else:
                    last_pivot_row = pivot

            left = 0

            if row_mode:
                column = pivot_column
                row_mode = False
                right = m - 1

            else:
                row = pivot_row
                row_mode = True
                right = n - 1
