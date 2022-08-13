class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        N = len(nums)
        dp = [1 for _ in range(N)]

        for i in range(1, N):

            for j in range(i):

                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
    