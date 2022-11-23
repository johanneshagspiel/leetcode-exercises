class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row_set = [set() for _ in range(9)]
        column_set = [set() for _ in range(9)]
        cell_set = [set() for _ in range(9)]

        for row in range(9):
            for column in range(9):
                content = board[row][column]

                if content != ".":
                    cell_number = (row // 3) * 3 + (column // 3)

                    if content in row_set[row]:
                        return False
                    else:
                        row_set[row].add(content)

                    if content in column_set[column]:
                        return False
                    else:
                        column_set[column].add(content)

                    if content in cell_set[cell_number]:
                        return False
                    else:
                        cell_set[cell_number].add(content)

        return True