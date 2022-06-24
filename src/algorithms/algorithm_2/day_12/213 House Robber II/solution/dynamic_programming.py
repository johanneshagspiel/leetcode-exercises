from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def helper(nums, start_index, n, mem_dic):

            if start_index > n:
                return 0
            elif start_index == n:
                return nums[start_index]
            elif start_index in mem_dic:
                return mem_dic[start_index]
            else:
                go_here = nums[start_index] + helper(nums, start_index + 2, n, mem_dic)
                not_go_here = helper(nums, start_index + 1, n, mem_dic)

                mem_dic[start_index] = max(go_here, not_go_here)
                return mem_dic[start_index]

        skip_first_house = helper(nums[1:], 0, len(nums) - 2, {})
        rob_first_house = helper(nums[:-1], 0, len(nums) - 2, {})

        return max(skip_first_house, rob_first_house)
