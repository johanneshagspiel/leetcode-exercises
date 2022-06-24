import heapq
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        priority_list = []
        for num in nums:
            heapq.heappush(priority_list, num)

            while len(priority_list) > k:
                heapq.heappop(priority_list)

        return priority_list[0]
