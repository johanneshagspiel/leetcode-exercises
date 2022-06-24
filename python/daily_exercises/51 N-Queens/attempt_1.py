class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def create_board(state):
            board = []
            for row in state:
                board.append("".join(row))
            return board

        def back_tracking(row, column_set, diagonal_set, anti_diagonal_set, state):

            if row == n:
                answer.append(create_board(state))
                return

            for column in range(n):
                current_diagonal = row - column
                current_anti_diagonal = row + column

                if (column in column_set) or (current_anti_diagonal in anti_diagonal_set) or (
                        current_diagonal in diagonal_set):
                    continue

                state[row][column] = "Q"
                column_set.add(column)
                diagonal_set.add(current_diagonal)
                anti_diagonal_set.add(current_anti_diagonal)

                back_tracking(row + 1, column_set, diagonal_set, anti_diagonal_set, state)

                state[row][column] = "."
                column_set.remove(column)
                diagonal_set.remove(current_diagonal)
                anti_diagonal_set.remove(current_anti_diagonal)

        column_set = set()
        diagonal_set = set()
        anti_diagonal_set = set()
        state = [["."] * n for row in range(n)]
        answer = []
        back_tracking(0, set(), set(), set(), state)

        return answer
