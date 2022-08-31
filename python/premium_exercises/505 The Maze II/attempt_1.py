import collections
import copy
from typing import List


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:

        rows = len(maze)
        columns = len(maze[0])

        def generate_moves(start_row, start_column, start_path_length):

            result = []

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for row_move, column_move in directions:

                begin_row = start_row
                begin_column = start_column
                begin_path_length = start_path_length

                while begin_row >=0 and begin_row < rows and begin_column >= 0 and begin_column < columns and maze[begin_row][begin_column] != 1:
                    begin_row += row_move
                    begin_column += column_move
                    begin_path_length += 1

                if begin_row - row_move != start_row or begin_column - column_move != start_column:
                    result.append((begin_row - row_move, begin_column - column_move, begin_path_length-1))

            return result

        queue = collections.deque()
        queue.appendleft((start[0], start[1], 0, set()))

        min_path = float("inf")

        while queue:

            queue_size = len(queue)

            for element in range(queue_size):

                current_row, current_column, current_path_length, current_seen_set = queue.pop()
                current_seen_set.add((current_row, current_column))

                if current_row == destination[0] and current_column == destination[1]:
                    min_path = min(min_path, current_path_length)
                else:
                    possible_moves = generate_moves(current_row, current_column, current_path_length)

                    for possible_row_move, possible_column_move, new_path_length in possible_moves:
                        if (possible_row_move, possible_column_move) not in current_seen_set:
                            queue.append((possible_row_move, possible_column_move, new_path_length, copy.deepcopy(current_seen_set)))

        return min_path if min_path != float("inf") else -1
