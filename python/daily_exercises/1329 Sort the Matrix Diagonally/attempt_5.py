class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:

        rows = len(mat)
        columns = len(mat[0])

        def sort_diagonal(start_row, start_column):
            diagonal = []

            current_row = start_row
            current_column = start_column

            while current_row >= 0 and current_column >= 0:
                diagonal.append(mat[current_row][current_column])

                current_row -= 1
                current_column -= 1

            diagonal.sort()

            current_row = start_row
            current_column = start_column

            while current_row >= 0 and current_column >= 0:
                mat[current_row][current_column] = diagonal.pop()

                current_row -= 1
                current_column -= 1

        for column in range(columns):
            sort_diagonal(rows-1, column)

        for row in range(rows-2, -1, -1):
            sort_diagonal(row, columns-1)

        return mat
