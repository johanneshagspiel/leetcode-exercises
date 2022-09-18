from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        left_to_right = []
        left_max_height = 0

        for current_height in height:

            if current_height > left_max_height:
                left_max_height = current_height

            saved = max(0, left_max_height - current_height)
            left_to_right.append(saved)


        right_to_left = []
        right_max_height = 0

        right_height = height[::-1]

        for current_height in right_height:

            if current_height > right_max_height:
                right_max_height = current_height

            saved = max(0, right_max_height - current_height)
            right_to_left.append(saved)

        right_to_left = right_to_left[::-1]

        res = []
        n = len(left_to_right)

        for position in range(n):
            saved_water = min(left_to_right[position], right_to_left[position])
            res.append(saved_water)

        return sum(res)
