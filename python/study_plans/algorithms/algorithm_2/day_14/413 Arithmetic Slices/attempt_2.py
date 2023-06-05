from typing import List
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        n = len(nums)

        distance_list = [nums[index+1] - nums[index] for index in range(n-1)]

        if len(distance_list) == 0:
            return 0

        elif len(distance_list) == 1:
            return 0

        else:
            compare_value = distance_list[0]
            total_length = 1

            total_sequences = 0

            for entry in distance_list[1:]:
                if entry == compare_value:
                    total_length += 1
                    if total_length >= 2:
                        total_sequences += total_length - 1

                else:
                    compare_value = entry
                    total_length = 1

            return total_sequences