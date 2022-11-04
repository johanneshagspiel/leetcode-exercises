class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:

        rows = len(grid)
        max_column = len(grid[0])

        columns = [(x, x) for x in range(len(grid[0]))]
        next_position = [(0, 0) for _ in range(len(grid[0]))]
        to_skip_col = {}

        for row in range(rows):
            for index, column in columns:
                if column != -1:
                    move = grid[row][column]
                    new_position = column + move

                    if new_position == max_column or new_position == -1:
                        next_position[index] = (index, -1)
                    else:
                        next_move = grid[row][column + move]

                        if next_move + move == 0:
                            next_position[index] = (index, -1)
                        else:

                            next_position[index] = (index, column + move)
            columns = next_position

        return [x[1] for x in columns]
