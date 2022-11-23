class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row_list = [0] * 9
        column_list = [0] * 9
        cell_list = [0] * 9

        for row in range(9):
            for column in range(9):

                if board[row][column] != ".":
                    number = int(board[row][column]) - 1
                    cell = (row // 3) * 3 + (column // 3)

                    row_bit = 1 << number
                    if row_list[row] & row_bit:
                        return False
                    else:
                        row_list[row] |= row_bit

                    column_bit = 1 << number
                    if column_list[column] & column_bit:
                        return False
                    else:
                        column_list[column] |= column_bit

                    cell_bit = 1 << number
                    if cell_list[cell] & cell_bit:
                        return False
                    else:
                        cell_list[cell] |= cell_bit

        return True
