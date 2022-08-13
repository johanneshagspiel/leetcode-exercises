from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        N = len(nums)
        dp = [[0]*N for _ in range(N)]

        result_list = []
        it = 0

        for i in range(N-1, -1, -1):
            for j in range(0, N, 1):

                if i == N-1:
                    if nums[j] > nums[i]:
                        dp[i][j] = 1

                else:
                    if nums[j] > nums[i]:
                        dp[i][j] = 1 + dp[i+1][j]
                    else:
                        dp[i][j] = dp[i+1][j]

            result_list.append(dp[i-it][j-it])
            it += 1

        return result_list[::-1]

