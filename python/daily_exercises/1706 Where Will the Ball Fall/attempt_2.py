class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:

        rows = len(grid)
        max_column = len(grid[0])

        result = [x for x in range(len(grid[0]))]

        for row in range(rows):
            for index, column in enumerate(result):
                if column != -1:
                    move = grid[row][column]
                    new_position = column + move

                    if new_position == max_column or new_position == -1:
                        result[index] = -1
                    else:
                        next_move = grid[row][new_position]

                        if next_move + move == 0:
                            result[index] = -1

                        else:
                            result[index] = column + move

        return result
