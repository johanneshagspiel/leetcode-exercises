class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player

        final_diagonal_win = True
        final_anti_diagonal_win = True
        final_column_win = True
        final_row_win = True

        for check in range(self.n):
            diagonal_win = self.board[0 + check][0 + check] == player
            if final_diagonal_win:
                final_diagonal_win = diagonal_win

            anti_diagonal_win = self.board[self.n - 1 - check][self.n - 1 - check] == player
            if final_anti_diagonal_win:
                final_anti_diagonal_win = anti_diagonal_win

            column_win = self.board[row][check] == player
            if final_column_win:
                final_column_win = column_win

            row_win = self.board[check][col] == player
            if final_row_win:
                final_row_win = row_win

            if not any([final_row_win, final_column_win, final_diagonal_win, final_anti_diagonal_win]):
                return 0

        if any([final_row_win, final_column_win, final_diagonal_win, final_anti_diagonal_win]):
            return player
        else:
            return 0
