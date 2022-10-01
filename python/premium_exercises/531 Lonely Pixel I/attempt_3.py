from typing import List


class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:

        rows = len(picture)
        columns = len(picture[0])

        for row in range(rows):
            for column in range(columns):

                pixel = picture[row][column]

                if row == 0 or column == 0:
                    if pixel == "B":
                        picture[row][column] = 1
                    else:
                        picture[row][column] = 0

                else:
                    if pixel == "B":
                        picture[0][column] += 1
                        picture[row][0] += 1

        res = 0

        for row in range(rows):
            for column in range(columns):
                pixel = picture[row][column]

                if pixel == "B":
                    if picture[0][column] == 1 and picture[row][0] == 1:
                        res += 1

        return res
