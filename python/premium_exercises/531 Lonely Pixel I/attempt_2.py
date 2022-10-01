class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:

        rows = len(picture)
        columns = len(picture[0])

        row_list = [0 for _ in range(rows)]
        column_list = [0 for _ in range(columns)]

        for row in range(rows):
            for column in range(columns):
                pixel = picture[row][column]

                if pixel == 'B':
                    row_list[row] += 1
                    column_list[column] += 1

        res = 0

        for row in range(rows):
            for column in range(columns):
                pixel = picture[row][column]

                if pixel == 'B':
                    if row_list[row] == 1 and column_list[column] == 1:
                        res += 1

        return res
