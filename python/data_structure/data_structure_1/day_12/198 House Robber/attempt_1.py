from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        else:
            dp = {}
            dp[0] = nums[0]
            dp[1] = nums[1]
            max_steal = max(nums[0], nums[1])

            n = len(nums)

            for number in range(2, n):
                if number > 2:
                    current_entry = max(dp[number - 1], nums[number] + max([dp[key] for key in range(0, number - 1)]))
                else:
                    current_entry = max(dp[number - 1], nums[number] + dp[number - 2])
                max_steal = max(max_steal, current_entry)
                dp[number] = current_entry

            return max_steal