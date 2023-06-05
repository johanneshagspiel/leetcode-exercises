from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1

        max_left = 0
        max_right = 0

        solution = 0

        while left <= right:

            if max_left < max_right:

                if height[left] > max_left:
                    max_left = height[left]
                else:
                    solution += max_left - height[left]

                left += 1

            else:

                if height[right] > max_right:
                    max_right = height[right]
                else:
                    solution += max_right - height[right]

                right -= 1

        return solution

