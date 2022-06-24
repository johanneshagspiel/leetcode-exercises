from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n_rows = len(isConnected)
        n_col = len(isConnected)
        visited_set = set()
        provinces = 0

        def bfs(row, column):
            moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            stack = []
            stack.append((row, column))

            while stack:
                current_row, current_column = stack.pop()

                for row_move, column_move in moves:
                    new_row = current_row + row_move
                    new_column = current_column + column_move

                    if new_row >= 0 and new_row < n_rows and new_column >= 0 and new_column < n_col:
                        new_entry = isConnected[new_row][new_column]
                        new_key = str(new_row) + "_" + str(new_column)

                        if new_entry == 1:
                            if new_key not in visited_set:
                                visited_set.add(new_key)
                                stack.append((new_row, new_column))

        for row in range(n_rows):
            for column in range(n_col):
                entry = isConnected[row][column]
                key = str(row) + "_" + str(column)

                if entry == 1:
                    if key not in visited_set:
                        provinces += 1
                        visited_set.add(key)
                        bfs(row, column)

        return provinces

if __name__ == "__main__":
    solution = Solution()
    print(solution.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))

