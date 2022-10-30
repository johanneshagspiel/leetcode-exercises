import collections


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        rows = len(grid)
        columns = len(grid[0])

        queue = collections.deque()
        queue.append((0, 0, 0, k, set()))

        moves = [(1,0),(-1,0),(0,1),(0,-1)]

        while queue:

            queue_len = len(queue)

            for _ in range(queue_len):

                current_row, current_column, current_moves, current_removable_obstacles, seen_cell_set = queue.popleft()

                if current_row == (rows-1) and current_column == (columns-1):
                    return current_moves

                else:
                    for row_move, column_move in moves:
                        new_row = current_row + row_move
                        new_column = current_column + column_move

                        if new_row >= 0 and new_row < rows and new_column >= 0 and new_column < columns:

                                new_cell = grid[new_row][new_column]

                                if new_cell == 0:

                                    if (new_row, new_column, current_removable_obstacles) not in seen_cell_set:

                                        seen_cell_set.add((new_row, new_column, current_removable_obstacles))

                                        queue.append((new_row, new_column, current_moves + 1, current_removable_obstacles, seen_cell_set))

                                elif current_removable_obstacles > 0:

                                    if (new_row, new_column, current_removable_obstacles - 1) not in seen_cell_set:

                                        seen_cell_set.add((new_row, new_column, current_removable_obstacles - 1))

                                        queue.append((new_row, new_column, current_moves + 1, current_removable_obstacles - 1, seen_cell_set))

        return -1
