from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        columns = len(board[0])

        def back_track(row, column, word):

            if len(word) == 0:
                return True

            moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            if word[0] == board[row][column]:
                board[row][column] = "#"

                for row_move, column_move in moves:
                    new_row = row + row_move
                    new_column = column + column_move

                    if new_row >= 0 and new_row < rows and new_column >= 0 and new_column < columns:
                        res = back_track(new_row, new_column, word[1:])

                        if res:
                            break
                board[row][column] = word[0]
                return res
            else:
                return False

        for row in range(rows):
            for column in range(columns):
                if back_track(row, column, word):
                    return True

        return False

