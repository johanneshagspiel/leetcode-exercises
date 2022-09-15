import copy
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(start_row, start_column, reverse_word ):

            reverse_word_list = list(reverse_word)

            visited = set()

            stack = []
            stack.append((start_row, start_column, reverse_word_list, visited))

            moves = [(1,0), (-1,0), (0,1), (0,-1)]

            while stack:
                current_row, current_column, current_word_list, visited = stack.pop()
                visited.add((current_row, current_column))
                current_word_list.pop()

                if len(current_word_list) == 0:
                    return True
                else:

                    for row_move, column_move in moves:
                        new_row = current_row + row_move
                        new_column = current_column + column_move

                        if new_row >= 0 and new_row < rows and new_column >= 0 and new_column < columns:
                            if board[new_row][new_column] == current_word_list[-1]:
                                if (new_row, new_column) not in visited:
                                    stack.append((new_row, new_column, copy.deepcopy(current_word_list), copy.deepcopy(visited)))

            return False


        first_char = word[0]

        reverse_word = word[::-1]

        rows = len(board)
        columns = len(board[0])

        for row in range(rows):
            for column in range(columns):
                if board[row][column] == first_char:
                    result = dfs(row, column, reverse_word)

                    if result:
                        return result

        return False
