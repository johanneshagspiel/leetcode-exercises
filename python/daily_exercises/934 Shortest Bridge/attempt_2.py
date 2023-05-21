import collections


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        n = len(grid)
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(startRow, startColumn):

            stack = []
            stack.append((startRow, startColumn))

            islandCells = []

            while stack:
                currentRow, currentColumn = stack.pop()
                grid[currentRow][currentColumn] = 2
                islandCells.append((currentRow, currentColumn))

                for rowMove, columnMove in moves:
                    newRow = currentRow + rowMove
                    newColumn = currentColumn + columnMove

                    if newRow > -1 and newRow < n and newColumn > -1 and newColumn < n:
                        newCell = grid[newRow][newColumn]

                        if newCell == 1:
                            stack.append((newRow, newColumn))

            return islandCells

        def bfs(startCellList):

            queue = collections.deque()

            for row, column in startCellList:
                queue.append((row, column))
                grid[row][column] = -1

            currentDistance = 0

            while queue:

                queueLength = len(queue)

                for element in range(queueLength):

                    currentRow, currentColumn = queue.popleft()

                    for rowMove, columnMove in moves:
                        newRow = currentRow + rowMove
                        newColumn = currentColumn + columnMove

                        if newRow > -1 and newRow < n and newColumn > -1 and newColumn < n:
                            newCell = grid[newRow][newColumn]

                            if newCell == 1:
                                return currentDistance

                            elif newCell == 0:
                                grid[newRow][newColumn] = -1
                                queue.append((newRow, newColumn))

                currentDistance += 1

        startRow = -1
        startColumn = -2

        for row in range(n):
            for column in range(n):
                cell = grid[row][column]

                if cell == 1:
                    startRow = row
                    startColumn = column
                    break

        islandCellsList = dfs(startRow, startColumn)
        return bfs(islandCellsList)