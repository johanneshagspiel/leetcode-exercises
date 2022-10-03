class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:

        rows = len(picture)
        columns = len(picture[0])

        row_list = [0 for _ in range(rows)]
        column_list = [0 for _ in range(columns)]

        for row in range(rows):
            for column in range(columns):
                pixel = picture[row][column]

                if pixel == "B":
                    row_list[row] += 1
                    column_list[column] += 1

        lonely_pixel = 0

        for row in range(rows):
            for column in range(columns):
                pixel = picture[row][column]

                if pixel == "B":
                    row_count = row_list[row]
                    column_count = column_list[column]

                    if row_count == 1 and column_count == 1:
                        lonely_pixel += 1

        return lonely_pixel
