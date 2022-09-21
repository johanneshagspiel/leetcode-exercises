import collections
import math


class TicTacToe:

    def __init__(self, n: int):
        self.rows = {}
        self.columns = {}

        self.diagonals = {}
        self.anti_diagonals = {}

        self.target = n

    def move(self, row: int, col: int, player: int) -> int:

        diagonal = row - col
        anti_diagonal = row + col

        if diagonal not in self.diagonals:
            self.diagonals[diagonal] = []
            self.diagonals[diagonal].append(0)
            self.diagonals[diagonal].append(0)

        if anti_diagonal not in self.anti_diagonals:
            self.anti_diagonals[anti_diagonal] = []
            self.anti_diagonals[anti_diagonal].append(0)
            self.anti_diagonals[anti_diagonal].append(0)

        if col not in self.columns:
            self.columns[col] = []
            self.columns[col].append(0)
            self.columns[col].append(0)

        if row not in self.rows:
            self.rows[row] = []
            self.rows[row].append(0)
            self.rows[row].append(0)


        if player == 1:
            self.rows[row][0] += 1
            self.columns[col][0] += 1
            self.diagonals[diagonal][0] += 1
            self.anti_diagonals[anti_diagonal][0] += 1

            if self.rows[row][0] == self.target \
                    or self.columns[col][0]  == self.target \
                    or self.diagonals[diagonal][0] == self.target \
                    or self.anti_diagonals[anti_diagonal][0] == self.target:
                return 1
            else:
                return 0

        else:
            self.rows[row][1] += 1
            self.columns[col][1] += 1
            self.diagonals[diagonal][1] += 1
            self.anti_diagonals[anti_diagonal][1] += 1

            if self.rows[row][1] == self.target \
                    or self.columns[col][1] == self.target \
                    or self.diagonals[diagonal][1] == self.target \
                    or self.anti_diagonals[anti_diagonal][1] == self.target:
                return 2
            else:
                return 0
