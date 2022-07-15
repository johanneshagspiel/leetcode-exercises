import heapq
from typing import List
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:

        N = len(nums)

        dp = [0 for _ in range(N)]
        dp[-1] = nums[-1]

        priority_list = []
        heapq.heappush(priority_list, (-dp[-1], N-1))

        for i in range(N-2, -1, -1):
            max_end = min(i+k, N-1)

            while priority_list[1] > max_end:
                heapq.heappop(priority_list)

            max_score = priority_list[0]
            dp[i] = nums[i] + max_score
            heapq.heappush(priority_list, (-dp[i], i))

        return dp[0]