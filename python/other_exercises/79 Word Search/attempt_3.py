from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        columns = len(board[0])

        def back_track(row, column, word):

            if len(word) == 0:
                return True

            if row < 0 or row >= rows or column < 0 or column >= columns or board[row][column] != word[0]:
                return False


            board[row][column] = "#"

            moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            res = False

            for row_move, column_move in moves:
                new_row = row + row_move
                new_column = column + column_move

                res = back_track(new_row, new_column, word[1:])

                if res:
                    break

            board[row][column] = word[0]
            return res



        for row in range(rows):
            for column in range(columns):
                if back_track(row, column, word):
                    return True

        return False
