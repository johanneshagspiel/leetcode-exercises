import collections
from typing import List


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

        rows = len(maze)
        columns = len(maze[0])

        visited = set()
        visited.add((start[0], start[1]))

        queue = collections.deque()
        queue.append((start[0], start[1]))

        while queue:
            current_row, current_column = queue.popleft()

            if (current_row == destination[0]) and (current_column == destination[1]):
                return True
            else:

                for delta in [-1, 1]:

                    anchor_row = current_row
                    anchor_column = current_column
                    while anchor_column + delta < columns and anchor_column + delta >= 0 and maze[anchor_row][anchor_column + delta] == 0:
                        anchor_column += delta

                    if (anchor_row, anchor_column) not in visited:
                        visited.add((anchor_row, anchor_column))
                        queue.append((anchor_row, anchor_column))


                    anchor_row = current_row
                    anchor_column = current_column
                    while anchor_row + delta < rows and anchor_row + delta >= 0 and maze[anchor_row + delta][anchor_column] == 0:
                        anchor_row += delta

                    if (anchor_row, anchor_column) not in visited:
                        visited.add((anchor_row, anchor_column))
                        queue.append((anchor_row, anchor_column))

        return False
