from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        answers = []

        def create_output_format(state):
            output = []

            for row in range(n):
                output.append("".join(state[row]))

            return output


        def back_track(row, column_set, diagonal_set, anti_diagonal_set, state):
            if row == n:
                answers.append(create_output_format(state))
                return

            for column in range(n):
                current_diagonal = row - column
                current_anti_diagonal = row + column

                if (column in column_set) or (current_diagonal in diagonal_set) or (current_anti_diagonal in anti_diagonal_set):
                    continue

                state[row][column] = "Q"
                column_set.add(column)
                diagonal_set.add(current_diagonal)
                anti_diagonal_set.add(current_anti_diagonal)

                back_track(row + 1, column_set, diagonal_set, anti_diagonal_set, state)

                state[row][column] = "."
                column_set.remove(column)
                diagonal_set.remove(current_diagonal)
                anti_diagonal_set.remove(current_anti_diagonal)

        state = [["."]*n for row in range(n)]
        back_track(0, set(), set(), set(), state)
        return answers

if __name__ == "__main__":
    solution = Solution()
    n = 4
    output = solution.solveNQueens(n)
    print(output)