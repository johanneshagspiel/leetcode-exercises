import heapq
import math
from typing import List


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:

        N = len(nums)

        dp = [math.inf for _ in range(N)]
        dp[-1] = nums[-1]

        priority_list = []
        heapq.heappush(priority_list, (-nums[-1], N-1))

        for position in range(N-2, -1, -1):

            while priority_list[0][1] > position + k:
                heapq.heappop(priority_list)

            dp[position] = nums[position] + (-1) * priority_list[0][0]
            heapq.heappush(priority_list, (-dp[position], position))

        return dp[0]

