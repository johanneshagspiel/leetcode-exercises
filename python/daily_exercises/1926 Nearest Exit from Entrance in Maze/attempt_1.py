class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        max_rows = len(maze)
        max_columns = len(maze[0])

        start_row = entrance[0]
        start_column = entrance[1]

        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        seen_set = set()
        queue = collections.deque()

        queue.append((start_row, start_column, 0))
        seen_set.add((start_row, start_column))

        while queue:

            len_queue = len(queue)

            for _ in range(len(queue)):

                row, column, steps = queue.popleft()

                if row == 0 or row == max_rows - 1:
                    if (row != start_row) or (column != start_column):
                        return steps
                if column == 0 or column == max_columns - 1:
                    if (row != start_row) or (column != start_column):
                        return steps

                for row_move, column_move in moves:
                    new_row = row + row_move
                    new_column = column + column_move

                    if new_row < max_rows and new_row >= 0 and new_column < max_columns and new_column >= 0:
                        if (new_row, new_column) not in seen_set:
                            cell = maze[new_row][new_column]

                            if cell != "+":
                                seen_set.add((new_row, new_column))
                                queue.append((new_row, new_column, steps + 1))

        return -1
