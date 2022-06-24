import math
from typing import List

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:

        moves = [(2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
        start_x = 0
        start_y = 0
        move_counter = 0

        while start_x != x or start_y != y:

            distance_list = []
            final_reach_found = False
            final_moves = 0

            for x_move, y_move in moves:

                new_x = start_x + x_move
                new_y = start_y + y_move

                if new_x > 0 and new_y > 0:

                    if new_x == x and new_y == y:
                        move_counter += 1

                        return move_counter

                    else:
                        can_reach_final, new_final_moves = self.look_ahead_three(x, y, new_x, new_y)

                        if can_reach_final:
                            final_reach_found = True
                            final_moves = new_final_moves + 1

                        else:
                            distance_x = x - (start_x + x_move)
                            distance_y = y - (start_y + y_move)

                            combined_distance = math.sqrt(pow(distance_x, 2) + pow(distance_y, 2))

                            distance_list.append((combined_distance, x_move, y_move))

            if final_reach_found:
                move_counter += final_moves
                return move_counter

            else:
                distance_min_move = min(distance_list, key=lambda x: x[0])

                start_x = start_x + distance_min_move[1]
                start_y = start_y + distance_min_move[2]

                move_counter += 1

        return move_counter


    def look_ahead_three(self, x: int, y: int, start_x: int, start_y: int):
        moves = [(2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

        for x_move, y_move in moves:
            if start_x + x_move == x and start_y + y_move == y:
                return True, 1
            else:
                two_ahead_boolean, two_ahead_moves = self.look_ahead_two(x, y, start_x + x_move, start_y + y_move)
                if two_ahead_boolean:
                    return True, two_ahead_moves + 1
        return False, 0


    def look_ahead_two(self, x: int, y: int, start_x: int, start_y: int):
        moves = [(2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

        for x_move, y_move in moves:
            if start_x + x_move == x and start_y + y_move == y:
                return True, 1
            else:
                one_ahead_boolean, one_ahead_moves = self.look_ahead_one(x, y, start_x + x_move, start_y + y_move)
                if one_ahead_boolean:
                    return True, one_ahead_moves + 1
        return False, 0


    def look_ahead_one(self, x: int, y: int, start_x: int, start_y: int):
        moves = [(2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

        for x_move, y_move in moves:
            if start_x + x_move == x and start_y + y_move == y:
                return True, 1
        return False, 0



if __name__ == '__main__':
    solution = Solution()
    x = 1
    y = 1
    output = solution.minKnightMoves(x, y)
    print(output)