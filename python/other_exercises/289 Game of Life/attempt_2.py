from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def get_surrounding(row, column):

            moves = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
            acc = 0
            for row_move, column_move in moves:
                new_row = row + row_move
                new_column = column + column_move

                if new_row >= 0 and new_row < m and new_column >= 0 and new_column < n:
                    if abs(board[new_row][new_column]) == 1:
                        acc += 1

            return acc


        m = len(board)
        n = len(board[0])


        for row in range(m):
            for column in range(n):
                sum_surrounding = get_surrounding(row, column)

                if board[row][column] == 0:
                    if sum_surrounding == 3:
                        board[row][column] = 2
                    else:
                        board[row][column] = 0

                else:
                    if sum_surrounding < 2:
                        board[row][column] = -1
                    if sum_surrounding == 2:
                        board[row][column] = 1
                    elif sum_surrounding == 3:
                        board[row][column] = 1
                    elif sum_surrounding > 3:
                        board[row][column] = -1

        for row in range(m):
            for column in range(n):
                cur_val = board[row][column]

                if cur_val > 0:
                    board[row][column] = 1
                else:
                    board[row][column] = 0

        return board
