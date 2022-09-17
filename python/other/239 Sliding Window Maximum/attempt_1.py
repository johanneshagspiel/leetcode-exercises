import collections
import heapq
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)

        heap = [((-1)*x, index) for index, x in enumerate(nums[:k])]
        heapq.heapify(heap)
        current_max = (-1)*heap[0][0]

        res = []
        res.append(current_max)

        for position in range(k+1, n, 1):
            heapq.heappush(heap, ((-1)*nums[position], position))

            while heap[0][1] < (position - k):
                heapq.heappop(heap)

            current_max = (-1) * heap[0][0]
            res.append(current_max)

        return res
