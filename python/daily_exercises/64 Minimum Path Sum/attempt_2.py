class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        columns = len(grid[0])

        for column in range(columns):
            for row in range(rows):
                top_move = float("inf")
                if row != 0:
                    top_move = grid[row-1][column]

                left_move = float("inf")
                if column != 0 :
                    left_move = grid[row][column-1]

                if column == 0 and row == 0:
                    grid[0][0] = grid[0][0]
                else:
                    grid[row][column] = grid[row][column] + min(top_move, left_move)

        return grid[-1][-1]
