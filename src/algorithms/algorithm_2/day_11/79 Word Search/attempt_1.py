from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        n_rows = len(board)
        n_col = len(board[0])

        first_letter = word[0]
        n_word = len(word)


        def dfs(start_row, start_column, move_amount, seen):

            moves = [(1,0),(-1,0),(0,1),(0,-1)]

            if move_amount == n_word:
                return True
            else:

                next_letter = word[move_amount]

                for row_move, column_move in moves:
                    new_row = start_row + row_move
                    new_column = start_column + column_move

                    if new_row >= 0 and new_row < n_rows and new_column >= 0 and new_column < n_col:
                        entry = board[new_row][new_column]
                        if entry == next_letter:
                            new_key = str(new_row) + "_" + str(new_column)

                            if new_key not in seen:
                                seen.add(new_key)
                                found = dfs(new_row, new_column, move_amount + 1, seen)
                                seen.remove(new_key)

                                if found:
                                    return True

            return False



        for row in range(n_rows):
            for column in range(n_col):
                letter = board[row][column]
                if letter == first_letter:

                    seen = set()
                    key = str(row) + "_" + str(column)
                    seen.add(key)
                    found = dfs(row, column, 1, seen)

                    if found:
                        return True

        return False
