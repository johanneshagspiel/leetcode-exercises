from typing import List


class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:

        res = 0

        rows = len(picture)
        columns = len(picture[0])

        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for row in range(rows):
            for column in range(columns):
                pixel = picture[row][column]

                if pixel == "B":
                    other_pixel_found = False

                    for row_move, column_move in moves:
                        new_row = row + row_move
                        new_column = column + column_move

                        if new_row >= 0 and new_row < rows and new_column >= 0 and new_column < columns:
                            other_pixel = picture[new_row][new_column]

                            if other_pixel == "B":
                                other_pixel_found = True
                                picture[new_row][new_column] = "X"

                    if not other_pixel_found:
                        res += 1
                    else:
                        picture[row][column] = "X"

        for row in range(rows):
            for column in range(columns):
                pixel = picture[row][column]

                if pixel == "X":
                    picture[row][column] = ' B'
                    
        return res
