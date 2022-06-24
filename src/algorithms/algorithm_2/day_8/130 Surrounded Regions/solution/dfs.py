import collections
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n_rows = len(board)
        n_cols = len(board[0])

        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        visited = set()

        def bfs(row, column):
            stack = []
            stack.append((row, column))
            visited.add((row, column))

            while stack:
                current_row, current_column = stack.pop()

                board[current_row][current_column] = "E"

                for row_move, column_move in moves:
                    new_row = current_row + row_move
                    new_column = current_column + column_move

                    if new_row >= 0 and new_row < n_rows and new_column >= 0 and new_column < n_cols:
                        new_key = str(new_row) + "-" + str(new_column)
                        if new_key not in visited:
                            new_entry = board[new_row][new_column]
                            if new_entry == 'O':
                                visited.add(new_key)
                                stack.append((new_row, new_column))

        for move_to_right in range(n_cols):
            key = str(0) + "-" + str(move_to_right)
            if key not in visited:
                position = board[0][move_to_right]
                if position == 'O':
                    bfs(0, move_to_right)
                visited.add(key)

        for move_bottom in range(n_rows):
            key = str(move_bottom) + "-" + str(n_cols - 1)
            if key not in visited:
                position = board[move_bottom][n_cols - 1]
                if position == 'O':
                    bfs(move_bottom, n_cols - 1)
                visited.add(key)

        for move_left in range(n_cols - 1, -1, -1):
            key = str(n_rows - 1) + "-" + str(move_left)
            if key not in visited:
                position = board[n_rows - 1][move_left]
                if position == 'O':
                    bfs(n_rows - 1, move_left)
                visited.add(key)

        for move_up in range(n_rows - 1, -1, -1):
            key = str(move_up) + "-" + str(0)
            if key not in visited:
                position = board[move_up][0]
                if position == 'O':
                    bfs(move_up, 0)
                visited.add(key)

        for row in range(n_rows):
            for column in range(n_cols):
                element = board[row][column]
                if element == "E":
                    board[row][column] = "O"
                else:
                    board[row][column] = "X"
