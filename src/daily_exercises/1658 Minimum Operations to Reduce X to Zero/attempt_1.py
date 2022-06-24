from typing import List
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        return self.min_operations_rec(nums, x, 0)

    def min_operations_rec(self, nums, x, pops):
        left_value = nums[0]
        right_value = nums[-1]

        if x - left_value == 0:
            return pops + 1
        elif x - right_value == 0:
            return pops + 1
        else:
            if x - left_value < 0 and x - right_value < 0:
                return
            elif x - left_value < 0 and x - right_value > 0:
                nums.pop(-1)
                right_side_min_pops = self.min_operations_rec(nums, x - right_value, pops + 1)
                nums.append(right_value)
                return right_side_min_pops
            elif x - left_value > 0 and x - right_value < 0:
                nums.pop(0)
                left_side_min_pops = self.min_operations_rec(nums, x - left_value, pops + 1)
                nums.insert(0, left_value)
                return left_side_min_pops
            elif x - left_value < 0 and x - right_value < 0:
                return
            else:
                nums.pop(-1)
                right_side_min_pops = self.min_operations_rec(nums, x - right_value, pops + 1)
                nums.append(right_value)
                nums.pop(0)
                left_side_min_pops = self.min_operations_rec(nums, x - left_value, pops + 1)
                nums.insert(0, left_value)
                return min(right_side_min_pops, left_side_min_pops)
