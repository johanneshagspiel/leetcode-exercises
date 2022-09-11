
class DUS():

    def __init__(self, grid):

        rows = len(grid)
        columns = len(grid[0])

        self.parent = [0 for _ in range(rows * columns)]
        self.rank = [0 for _ in range(rows * columns)]
        self.count = 0

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == "1":
                    self.parent[row*columns + column] = row*columns + column
                    self.count += 1


    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]


    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x == parent_y:
            return False
        else:
            rank_x = self.rank[parent_x]
            rank_y = self.rank[parent_y]

            if rank_y > rank_x:
                self.parent[parent_x] = parent_y

            elif rank_x > rank_y:
                self.parent[parent_x] = parent_y

            else:
                self.parent[parent_y] = parent_x
                self.rank[parent_x] += 1

            self.count -= 1
            return True

    def get_count(self):
        return self.count


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dus = DUS(grid)

        rows = len(grid)
        columns = len(grid[0])

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == "1":
                    grid[row][column] = "2"

                    for row_move, column_move in moves:
                        new_row = row + row_move
                        new_column = column + column_move

                        if new_row >= 0 and new_row < rows and new_column >= 0 and new_column < columns and grid[new_row][new_column] == "1":
                            dus.union(row*columns+column, new_row*columns+new_column)

        return dus.get_count()
