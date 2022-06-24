from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in range(0, 9):
            row_set = set()
            for column in range(0, 9):
                current_number = board[row][column]
                if current_number != ".":
                    if current_number in row_set:
                        return False
                    else:
                        row_set.add(current_number)
            del row_set

        for column in range(0, 9):
            column_set = set()
            for row in range(0, 9):
                current_number = board[row][column]
                if current_number != ".":
                    if current_number in column_set:
                        return False
                    else:
                        column_set.add(current_number)
            del column_set

        start_x = 0
        start_y = 0
        for sub_box in range(0, 9):
            if sub_box != 0:
                start_x += 3
                if start_x > 8:
                    start_x = 0
                    start_y += 3

            current_x = start_x
            current_y = start_y
            sub_set = set()
            for move in range(0, 9):
                current_number = board[current_x][current_y]
                if current_number != ".":
                    if current_number in sub_set:
                        return False
                    else:
                        sub_set.add(current_number)

                current_x += 1
                if current_x % 3 == 0:
                    current_x = current_x - 3
                    current_y += 1

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
