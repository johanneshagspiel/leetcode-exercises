import json
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:


        rows = len(heights)
        columns = len(heights[0])

        cell_dic = {}

        result = []


        def dfs(start_row, start_column):

            stack = []
            stack.append((start_row, start_column, heights[start_row][start_column]))

            moves = [(1,0), (-1,0), (0,1), (0,-1)]

            reach_pacific = False
            reach_atlantic = False

            seen_set = set()

            while stack:
                current_row, current_column, current_height = stack.pop()
                seen_set.add((current_row, current_column))

                if reach_pacific and reach_atlantic:
                    break

                for row_move, column_move in moves:
                    new_row = current_row + row_move
                    new_column = current_column + column_move

                    if (new_row, new_column) not in seen_set:

                        if new_row < 0 or new_column < 0:
                            reach_pacific = True

                        elif new_row >= rows or new_column >= columns:
                            reach_atlantic = True

                        else:
                            height_new_location = heights[new_row][new_column]

                            if height_new_location <= current_height:
                                if (new_row, new_column) in cell_dic:

                                    if cell_dic[(new_row, new_column)]["pacific"] == True:
                                        reach_pacific = True
                                    if cell_dic[(new_row, new_column)]["atlantic"] == True:
                                        reach_atlantic = True

                                else:
                                    stack.append((new_row, new_column, height_new_location))


            cell_dic[(start_row, start_column)] = {}
            cell_dic[(start_row, start_column)]["pacific"] = reach_pacific
            cell_dic[(start_row, start_column)]["atlantic"] = reach_atlantic

            if reach_pacific and reach_atlantic:
                result.append((start_row, start_column))


        for row in range(rows):
            for column in range(columns):

                if (row, column) not in cell_dic:

                    dfs(row, column)

        return result