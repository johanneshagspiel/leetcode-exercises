import copy
from typing import List


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

        rows = len(maze)
        columns = len(maze[0])

        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        stack = []

        visited = set()
        visited.add((start[0], start[1]))

        stack.append((start[0], start[1], visited))

        while stack:
            current_row, current_column, visited_set = stack.pop()

            if current_row == destination[0] and current_column == destination[1]:
                return True
            else:
                for row_move, column_move in moves:

                    anchor_row = current_row
                    anchor_column = current_column

                    while anchor_row >= 0 and anchor_row < rows and anchor_column >= 0 and anchor_column < columns and maze[anchor_row][anchor_column] == 0:
                        anchor_row += row_move
                        anchor_column += column_move

                    anchor_row -= row_move
                    anchor_column -= column_move

                    if (anchor_row, anchor_column) not in visited_set:
                        visited_set.add((anchor_row, anchor_column))
                        stack.append((anchor_row, anchor_column, visited_set))

        return False
