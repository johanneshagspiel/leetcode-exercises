from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)

        max_left_height = 0
        left_to_right = []

        for position in range(n):

            current_height = height[position]

            if current_height > max_left_height:
                max_left_height = current_height

            water_collection = max_left_height - current_height
            left_to_right.append(water_collection)

        max_right_height = 0
        right_to_left = []

        for position in range(n-1, -1, -1):

            current_height = height[position]

            if current_height > max_right_height:
                max_right_height = current_height

            water_collection = max_right_height - current_height
            right_to_left.append(water_collection)

        right_to_left = right_to_left[::-1]

        solution = []

        for index in range(len(left_to_right)):
            water_collected = min(left_to_right[index], right_to_left[index])
            solution.append(water_collected)

        return sum(solution)


