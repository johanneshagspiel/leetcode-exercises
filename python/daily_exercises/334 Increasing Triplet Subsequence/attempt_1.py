from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest_num = float("inf")
        second_smallest_num = float("inf")

        for num in nums:
            if num <= smallest_num:
                smallest_num = num
            elif num <= second_smallest_num:
                second_smallest_num = num
            else:
                return True

        return False