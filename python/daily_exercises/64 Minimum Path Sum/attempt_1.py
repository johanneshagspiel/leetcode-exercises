class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        columns = len(grid[0])

        new_grid = [[float("inf") for _ in range(columns)] for _ in range(rows)]

        for column in range(columns):
            for row in range(rows):
                top_move = float("inf")
                if row != 0:
                    top_move = new_grid[row-1][column]

                left_move = float("inf")
                if column != 0 :
                    left_move = new_grid[row][column-1]

                if column == 0 and row == 0:
                    new_grid[0][0] = grid[0][0]
                else:
                    new_grid[row][column] = grid[row][column] + min(top_move, left_move)

        return new_grid[-1][-1]
