from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9

        row_bit_mask = [0]*N
        column_bit_mask = [0]*N
        box_bit_mask = [0]*N

        for row in range(N):
            for column in range(N):

                if board[row][column] == ".":
                    continue

                value_at_current_position = int(board[row][column])

                row_bit = row_bit_mask[row]
                if row_bit & (1 << value_at_current_position):
                    return False
                row_bit_mask[row] |= (1 << value_at_current_position)

                column_bit = column_bit_mask[column]
                if column_bit & (1 << value_at_current_position):
                    return False
                column_bit_mask[column] |= (1 << value_at_current_position)

                box_id = (row // 3) * 3 + (column // 3)
                box_bit = box_bit_mask[box_id]
                if box_bit & (1 << value_at_current_position):
                    return False
                box_bit_mask[box_id] |= (1 << value_at_current_position)

        return True


if __name__ == "__main__":
    solution = Solution()

    board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

    output = solution.isValidSudoku(board)
    print(output)
