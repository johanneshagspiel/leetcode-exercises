class Solution:
    def totalNQueens(self, n: int) -> int:
        self.answers = 0
        self.n = n

        self.back_track(0, set(), set(), set())

        return self.answers


    def back_track(self, row, column_set, diagonal_set, anti_diagonal_set):

        if row == self.n:
            self.answers += 1
            return

        for column in range(self.n):

            diagonal_value = row - column
            anti_diagonal_value = row + column

            if (column in column_set) or (diagonal_value in diagonal_set) or (anti_diagonal_value in anti_diagonal_set):
                continue

            column_set.add(column)
            diagonal_set.add(diagonal_value)
            anti_diagonal_set.add(anti_diagonal_value)

            self.back_track(row + 1, column_set, diagonal_set, anti_diagonal_set)

            column_set.remove(column)
            diagonal_set.remove(diagonal_value)
            anti_diagonal_set.remove(anti_diagonal_value)

