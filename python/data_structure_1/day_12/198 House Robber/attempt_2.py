from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        def rob_helper(start_point, rob_dic):

            if start_point == n:
                return 0
            elif start_point in rob_dic:
                return rob_dic[start_point]
            else:
                value = max(rob_helper(start_point + 1, rob_dic), nums[start_point] + rob_helper(start_point + 2, rob_dic))
                rob_dic[start_point] = value
                return value

        return rob_helper(0, {})