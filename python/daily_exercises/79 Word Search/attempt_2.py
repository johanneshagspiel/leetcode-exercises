class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        max_rows = len(board)
        max_columns = len(board[0])
        found = False

        def back_track(row, column, index):

            nonlocal found
            moves = [(1,0),(-1,0),(0,1),(0,-1)]

            if index == len(word):
                found = True
            else:
                current_char = board[row][column]

                if current_char != word[index]:
                    return
                else:
                    board[row][column] = "#"

                    for row_move, column_move in moves:
                        new_row = row + row_move
                        new_column = column + column_move

                        if new_row >= 0 and new_row < max_rows and new_column >= 0 and new_column < max_columns:
                            back_track(new_row, new_column, index + 1)

                    board[row][column] = current_char

        if max_rows == 1 and max_columns == 1 and len(word) == 1:
            return board[0][0] == word[0]

        for row in range(max_rows):
            for column in range(max_columns):
                back_track(row, column, 0)
                if found:
                    return True

        return False