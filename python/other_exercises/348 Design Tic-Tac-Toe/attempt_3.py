import collections


class TicTacToe:

    def __init__(self, n: int):
        self.rows = [0 for _ in range(n)]
        self.columns = [0 for _ in range(n)]
        self.diagonal = 0
        self.anti_diagonal = 0
        self.target = n

    def move(self, row: int, col: int, player: int) -> int:

        if player == 1:
            current_player = 1
        else:
            current_player = -1

        self.rows[row] += current_player
        self.columns[col] += current_player

        if (row - col == 0):
            self.anti_diagonal += current_player

        if (row + col == self.target - 1):
            self.diagonal += current_player

        if abs(self.rows[row]) == self.target or abs(self.columns[col]) == self.target or abs(self.diagonal) == self.target or abs(self.anti_diagonal) == self.target:
            return player

        return 0
