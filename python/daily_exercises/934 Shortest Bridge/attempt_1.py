class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        n = len(grid)

        #Down
        downGrid = [[float("inf") for _ in range(n)] for _ in range(n)]
        for row in range(n):
            for column in range(n):
                cell = grid[row][column]

                if cell == 1:
                    downGrid[row][column] = 0
                else:
                    options = []
                    if column + 1 < n:
                        options.append(downGrid[row][column + 1])
                    if row + 1 < n:
                        options.append(downGrid[row + 1][column])
                    if column - 1 > -1:
                        options.append(downGrid[row][column - 1])
                    if row - 1 > -1:
                        options.append(downGrid[row - 1][column])

                    minOption = min(options)
                    if minOption < float("inf"):
                        downGrid[row][column] = 1 + min(options)

        #Up
        upGrid = [[float("inf") for _ in range(n)] for _ in range(n)]
        for row in range(n):
            for column in range(n -1, -1, -1):
                cell = grid[row][column]

                if cell == 1:
                    upGrid[row][column] = 0
                else:
                    options = []
                    if column + 1 < n:
                        options.append(upGrid[row][column + 1])
                    if row + 1 < n:
                        options.append(upGrid[row + 1][column])
                    if column - 1 > -1:
                        options.append(upGrid[row][column - 1])
                    if row - 1 > -1:
                        options.append(upGrid[row - 1][column])

                    minOption = min(options)
                    if minOption < float("inf"):
                        upGrid[row][column] = 1 + min(options)

        minUpDown = float("inf")
        for row in range(n):
            for column in range(n):
                option1 = upGrid[row][column]
                option2 = downGrid[row][column]

                maxOption = max(option1, option2)

                if minUpDown < float("inf"):
                    minUpDown = min(minUpDown, maxOption)

        return minUpDown



