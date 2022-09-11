class DS:

    def __init__(self, grid):

        rows = len(grid)
        columns = len(grid[0])

        self.rank = [0 for _ in range(rows * columns)]
        self.parent = [0 for _ in range(rows * columns)]
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
            rank_px = self.rank[parent_x]
            rank_py = self.rank[parent_y]

            if rank_px > rank_py:
                self.parent[parent_y] = parent_x

            elif rank_py > rank_px:
                self.parent[parent_x] = parent_y

            else:
                self.parent[parent_y] = parent_x
                self.rank[parent_x] += 1

            self.count -= 1

    def get_count(self):
        return self.count

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        columns = len(grid[0])
        dus = DS(grid)

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == "1":

                    grid[row][column] = "0"

                    for delta in [1, -1]:

                        if column + delta >= 0 and column + delta < columns and grid[row][column + delta] == "1":
                            dus.union(row*columns + column, row*columns + (column + delta))

                        if row + delta >= 0 and row + delta < rows and grid[row + delta][column] == "1":
                            dus.union(row*columns + column, (row + delta)*columns + column)

        return dus.get_count()
