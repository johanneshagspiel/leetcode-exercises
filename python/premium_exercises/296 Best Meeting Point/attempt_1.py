class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:

        rows_len = len(grid)
        columns_len = len(grid[0])

        rows = []
        columns = []

        for row in range(rows_len):
            for column in range(columns_len):
                if grid[row][column] == 1:
                    rows.append(row)
                    columns.append(column)

        median_row = rows[len(rows) // 2]
        columns.sort()
        median_column = columns[len(columns) // 2]

        min_distance = 0

        for (row, column) in zip(rows, columns):
            min_distance += abs(median_row - row) + abs(median_column - column)

        return min_distance