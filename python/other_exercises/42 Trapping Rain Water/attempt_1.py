from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        total_water = 0

        left_position = -1
        left_height = -1

        for index, curr_height in enumerate(height):
            if curr_height > 0:
                left_position = index
                left_height = curr_height
                break

        go_on = left_position != -1

        while go_on:

            wall_found = False
            right_side = height[(left_position + 1):]

            for potential_height in range(left_height, -1, -1):
                cur_water = 0

                for index, curr_height in enumerate(right_side):

                    if curr_height >= potential_height:
                        left_position = index
                        left_height = curr_height

                        wall_found = True
                        break
                    else:
                        cur_water += (potential_height - curr_height)

                if wall_found:
                    total_water += cur_water
                    break

            if not wall_found:
                go_on = False

        return total_water
