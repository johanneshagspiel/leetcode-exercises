import heapq
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [math.inf for _ in range(N)]
        dp[-1] = 0

        priority_list = []
        heapq.heappush(priority_list, (0, N-1))

        for position in range(N-2, -1, -1):
            jump_length = nums[position]
            if jump_length == 0:
                dp[position] = math.inf
            else:
                end_position = min(N-1, position + 1 + jump_length)

                while priority_list[0][1] > end_position:
                    heapq.heappop(priority_list)

                new_score = 1 + priority_list[0][0]
                dp[position] = new_score
                heapq.heappush(priority_list, (new_score, position))

        return dp[0]
