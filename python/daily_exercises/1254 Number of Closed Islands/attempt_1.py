class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

          visited_set = set()
          res = 0

          rows = len(grid)
          columns = len(grid[0])

          def dfs(start_row, start_column):
              closed_island = True

              stack = []
              stack.append((start_row, start_column))

              while stack:
                  row, column = stack.pop()

                  for row_move, column_move in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                      new_row = row + row_move
                      new_column = column + column_move

                      if new_row >= 0 and new_row < rows and new_column >= 0 and new_column < columns:
                        if (new_row, new_column) not in visited_set:
                            new_cell = grid[new_row][new_column]
                            if new_cell == 0:
                                stack.append((new_row, new_column))
                                visited_set.add((new_row, new_column))
                      else:
                          closed_island = False

              if closed_island:
                  return 1
              else:
                  return 0

          for row in range(rows):
              for column in range(columns):
                  cell = grid[row][column]

                  if (row, column) not in visited_set:
                      visited_set.add((row, column))

                      if cell == 0:
                          res += dfs(row, column)

          return res


