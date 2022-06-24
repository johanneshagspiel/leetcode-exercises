import math
from typing import List

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:

        moves = [(2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
        start_x = 0
        start_y = 0
        move_counter = 0

        if start_x == x and start_y == y:
            return 0

        else:

            to_check_moves = []

            for new_x_move, new_y_move in moves:

                if start_x + new_x_move > 0 and start_y + new_x_move > 0:
                    to_check_moves.append((new_x_move, new_y_move))

            result_list = []

            for new_x_move, new_y_move in to_check_moves:
                result = self.minKnightMoves_Helper(x, y, start_x, start_y, new_x_move, new_y_move) + 1
                result_list.append(result)

            return min(result_list)


    def minKnightMoves_Helper(self, target_x: int, target_y: int, start_x: int, start_y: int, x_move: int, y_move: int) -> int:

        moves = [(2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

        if start_x + x_move == target_x and start_y + y_move == target_y:
            return 1

        else:
            new_x = start_x + x_move
            new_y = start_y + y_move

            to_check_moves = []

            for new_x_move, new_y_move in moves:

                if new_x + new_x_move > 0 and new_y + new_x_move > 0:
                    to_check_moves.append((new_x_move, new_y_move))

            result_list = []

            for new_x_move, new_y_move in to_check_moves:
                result = self.minKnightMoves_Helper(target_x, target_y, new_x, new_y, new_x_move, new_y_move) + 1
                result_list.append(result)

            return min(result_list)





if __name__ == '__main__':
    solution = Solution()
    x = 5
    y = 5
    output = solution.minKnightMoves(x, y)
    print(output)