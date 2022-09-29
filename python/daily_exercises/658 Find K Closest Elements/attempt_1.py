import heapq
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        heap = []

        for num in arr:
            distance = abs(num - x)
            heapq.heappush(heap, (distance, num))

        res = heapq.nsmallest(k, heap)
        res = [x[1] for x in res]
        res.sort()
        return res
