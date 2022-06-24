from typing import List
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        n = len(heights)

        def furthest_building_rec(current_location, bricks, ladders, moves, move_dic):

            if current_location in move_dic:
                return move_dic[current_location]

            else:

                if current_location == (n - 1):
                    move_dic[current_location] = moves
                    return moves
                else:

                    height_current_location = heights[current_location]
                    height_next_location = heights[current_location + 1]

                    if height_next_location <= height_current_location:
                        down_move = furthest_building_rec(current_location + 1, bricks, ladders, moves + 1, move_dic)
                        move_dic[current_location] = down_move
                        return down_move

                    else:
                        height_difference = height_next_location - height_current_location
                        if ladders > 0:
                            ladder_move = furthest_building_rec(current_location + 1, bricks, ladders - 1, moves + 1, move_dic)
                        else:
                            ladder_move = moves

                        if height_difference <= bricks:
                            brick_move = furthest_building_rec(current_location + 1, bricks - height_difference, ladders, moves + 1, move_dic)
                        else:
                            brick_move = moves

                        move = max(ladder_move, brick_move)
                        move_dic[current_location] = move
                        return move

        return furthest_building_rec(0, bricks, ladders, 0, {})


