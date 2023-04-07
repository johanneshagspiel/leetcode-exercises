class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        columns = len(grid[0])
        visited_set = set()

        res = 0

        def dfs(start_row, start_column):

            stack = []
            stack.append((start_row, start_column))

            bound_reachable = False
            cells = 0

            while stack:
                row, column = stack.pop()
                cells += 1

                for row_move, column_move in [(1,0), (-1,0), (0,1), (0,-1)]:
                    new_row = row + row_move
                    new_column = column + column_move

                    if new_row >= 0 and new_row < rows and new_column >= 0 and new_column < columns:
                        if (new_row, new_column) not in visited_set:
                            new_cell = grid[new_row][new_column]

                            if new_cell == 1:
                                visited_set.add((new_row, new_column))
                                stack.append((new_row, new_column))
                    else:
                        bound_reachable = True

            if bound_reachable:
                return 0
            else:
                return cells


        for row in range(rows):
            for column in range(columns):
                cell = grid[row][column]

                if (row, column) not in visited_set:
                    visited_set.add((row, column))

                    if cell == 1:
                        res += dfs(row, column)

        return res
