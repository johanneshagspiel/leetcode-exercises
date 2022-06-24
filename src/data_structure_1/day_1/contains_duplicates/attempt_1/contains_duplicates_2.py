from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        if len(nums) != len(set(nums)):

            for index_start, current_number in enumerate(nums):

                for addition in range(1, k):
                    new_index = index_start + addition

                    if new_index < len(nums):
                        other_number = nums[new_index]

                        if current_number == other_number:
                            return True

        return False
