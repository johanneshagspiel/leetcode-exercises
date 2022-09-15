from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        self.rows = len(board)
        self.columns = len(board[0])
        self.board = board

        for row in range(self.rows):
            for column in range(self.columns):
                if self.back_track(row, column, word):
                    return True

        return False

    def back_track(self, row, column, word):

        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        if len(word) == 0:
            return True

        if row < 0 or row >= self.rows or column < 0 or column >= self.columns or self.board[row][column] != word[0]:
            return False

        res = False

        self.board[row][column] = "#"

        for row_move, column_move in moves:
            new_row = row + row_move
            new_column = column + column_move

            res = self.back_track(new_row, new_column, word[1:])

            if res:
                break

        self.board[row][column] = word[0]

        return res



