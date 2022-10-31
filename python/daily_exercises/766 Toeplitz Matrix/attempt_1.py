class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        rows = len(matrix)
        columns = len(matrix[0])

        def check_matrix(start_row, start_column):
            it_row = row
            it_column = start_column
            start_value = matrix[start_row][start_column]

            while it_row < rows and it_column < columns:
                new_value = matrix[it_row][it_column]
                if new_value != start_value:
                    return False
                else:
                    it_row += 1
                    it_column += 1

            return True

        for row in range(rows - 1, -1, -1):
            if not check_matrix(row, 0):
                return False

        for column in range(1, columns):
            if not check_matrix(0, column):
                return False

        return True
