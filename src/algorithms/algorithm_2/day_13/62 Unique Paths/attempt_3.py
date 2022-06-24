class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        row_target = m - 1
        col_target = n - 1

        self.moves = 1

        def rec(row, column):

            if row < row_target and column < col_target:
                self.moves += 1
                rec(row + 1, column)
                rec(row, column + 1)
            else:
                return 

            # if row == row_target and column == col_target:
            #     return
            #
            # elif row < row_target and column < col_target:
            #     self.moves += 1
            #     rec(row + 1, column)
            #     rec(row, column + 1)
            #
            # elif row < row_target:
            #     rec(row + 1, column)
            #
            # elif column < col_target:
            #     rec(row, column + 1)
            #
            # else:
            #     print("how?")

        rec(0, 0)
        return self.moves