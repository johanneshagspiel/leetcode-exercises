from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        res = []

        rows = len(heights)
        columns = len(heights[0])

        reachable_dic = {}

        def dfs(start_row, start_column):

            moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            path = set()
            path.add((start_row, start_column))

            stack = []
            stack.append((start_row, start_column))

            reached_atlantic = False
            reached_pacific = False

            while stack:
                current_row, current_column = stack.pop()
                current_height = heights[current_row][current_column]

                if reached_pacific and reached_atlantic:
                    break

                for row_move, column_move in moves:
                    new_row = current_row + row_move
                    new_column = current_column + column_move

                    if new_row == -1 or new_column == -1:
                        reached_pacific = True

                    if new_row == rows or new_column == columns:
                        reached_atlantic = True

                    if new_row >= 0 and new_row < rows and new_column >= 0 and new_column < columns and heights[new_row][new_column] <= current_height and (new_row, new_column) not in path:

                        if (new_row, new_column) in reachable_dic:

                            if reachable_dic[(new_row, new_column)]["atlantic"] == True:
                                reached_atlantic = True
                            if reachable_dic[(new_row, new_column)]["pacific"] == True:
                                reached_pacific = True

                        else:
                            path.add((new_row, new_column))
                            stack.append((new_row, new_column))

            reachable_dic[(start_row, start_column)] = {}
            reachable_dic[(start_row, start_column)]["atlantic"] = reached_atlantic
            reachable_dic[(start_row, start_column)]["pacific"] = reached_pacific

            if reached_pacific and reached_atlantic:
                res.append((start_row, start_column))

        for row in range(rows):
            for column in range(columns):
                dfs(row, column)

        return res
