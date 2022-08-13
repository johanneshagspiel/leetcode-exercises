from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def get_surrounding(row, column):

            moves = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, 1)]
            acc = 0
            for row_move, column_move in moves:
                new_row = row + row_move
                new_column = column + column_move

                if new_row >= 0 and new_row < m and new_column >= 0 and new_column < n:
                    acc += board[new_row][new_column]

            return acc


        m = len(board)
        n = len(board[0])

        res = [[0]*n for _ in range(m)]

        for row in range(m):
            for column in range(n):
                sum_surrounding = get_surrounding(row, column)

                if board[row][column] == 0:
                    if sum_surrounding == 3:
                        res[row][column] = 1

                else:
                    if sum_surrounding == 2:
                        res[row][column] = 1
                    elif sum_surrounding == 3:
                        res[row][column] = 1

        board[::] = res
