class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        max_columns = len(matrix[0])
        max_rows = len(matrix)

        lower_row = matrix[-1]
        new_row = [0]*max_rows

        for row in range(max_rows - 2, -1, -1):
            for column in range(max_columns):

                if column == 0:
                    left_col = lower_row[column]
                else:
                    left_col = lower_row[column - 1]

                middle_col = lower_row[column]

                if column == (max_columns - 1):
                    right_col = lower_row[column]
                else:
                    right_col = lower_row[column + 1]

                new_row[column] = matrix[row][column] + min(left_col, middle_col, right_col)

            lower_row = new_row
            new_row = [0]*max_rows

        return min(lower_row)

