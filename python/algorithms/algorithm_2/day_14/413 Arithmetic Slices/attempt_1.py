from typing import List
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        n = len(nums)
        if n < 3:
            return 0

        total_sequences = 0

        def look_out(distance, index):
            found = 0

            while index < n - 1 and (nums[index+1] - nums[index] == distance):
                found += 1
                index += 1

            return found


        for index in range(n - 2):
            if nums[index + 2] - nums[index + 1] == nums[index + 1] - nums[index]:
                distance = nums[index + 1] - nums[index]
                sequences = 1 + look_out(distance, index + 2)
                total_sequences += sequences

        return total_sequences