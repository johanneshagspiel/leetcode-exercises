class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        row_below = triangle[-1]
        rows = len(triangle)

        for row in range(rows-2, -1, -1):
            current_row = triangle[row]
            new_row_bellow = []
            for column in range(len(current_row)):
                new_entry = current_row[column] + min(row_below[column], row_below[column + 1])
                new_row_bellow.append(new_entry)
            row_below = new_row_bellow

        return row_below[0]
