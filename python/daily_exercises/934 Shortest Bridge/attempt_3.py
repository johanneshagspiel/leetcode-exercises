import collections


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        n = len(grid)
        moves = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(startRow, startColumn):

            result = []
            stack = [(startRow, startColumn)]

            grid[startRow][startColumn] = 2

            while stack:
                currentRow, currentColumn = stack.pop()

                result.append((currentRow, currentColumn))

                for rowMove, columnMove in moves:
                    newRow = currentRow + rowMove
                    newColumn = currentColumn + columnMove

                    if newRow > -1 and newRow < n and newColumn > -1 and newColumn < n:
                        newCell = grid[newRow][newColumn]

                        if newCell == 1:
                            grid[newRow][newColumn] = 2
                            stack.append((newRow, newColumn))

            return result

        def bfs(islandList):

            queue = collections.deque(islandList)

            distance = 0

            while queue:

                queue_len = len(queue)

                for element in range(queue_len):

                    currentRow, currentColumn = queue.popleft()

                    for rowMove, columnMove in moves:
                        newRow = currentRow + rowMove
                        newColumn = currentColumn + columnMove

                        if newRow > -1 and newRow < n and newColumn > -1 and newColumn < n:
                            newCell = grid[newRow][newColumn]

                            if newCell == 1:
                                return distance
                            elif newCell == 0:
                                grid[newRow][newColumn] = 2
                                queue.append((newRow, newColumn))

                distance += 1

        for row in range(n):
            for column in range(n):
                cell = grid[row][column]

                if cell == 1:
                    startRow, startColumn = row, column
                    break

        islandList = dfs(startRow, startColumn)
        return bfs(islandList)
