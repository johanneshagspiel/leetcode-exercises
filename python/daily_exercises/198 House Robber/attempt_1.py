class Solution:
    def rob(self, nums: List[int]) -> int:
        num_houses = len(nums)

        if num_houses == 1:
            return nums[0]
        elif num_houses == 2:
            return max(nums[0], nums[1])

        dp = [0] * num_houses
        dp[-1] = nums[-1]
        dp[-2] = max(nums[-2], nums[-1])

        for i in range(num_houses - 3, -1, -1):
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])

        return dp[0]
