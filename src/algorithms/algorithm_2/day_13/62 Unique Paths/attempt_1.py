class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        self.moves = 0

        n_row = m
        n_col = n

        def back_track(current_row, current_column):

            if current_row == n_row and current_column == n_col:
                self.moves += 1
                return
            else:
                if current_row < n_row and current_column < n_col:
                    back_track(current_row + 1, current_column)
                    back_track(current_row, current_column + 1)
                    return
                elif current_row < n_row:
                    return back_track(current_row + 1, current_column)
                elif current_column < n_col:
                    return back_track(current_row, current_column + 1)

        back_track(0, 0)
        return self.moves
