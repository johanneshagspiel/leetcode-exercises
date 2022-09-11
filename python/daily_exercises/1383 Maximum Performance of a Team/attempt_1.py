import heapq
from typing import List


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:

        tuple_list = list(zip(speed, efficiency))
        tuple_list.sort(key=lambda x:x[0], reverse = True)

        speed_sum = 0
        speed_heap = []

        res = 0

        for speed, efficiency in tuple_list:

            if len(speed_heap) > (k - 1):
                speed_sum -= heapq.heappop(speed_heap)

            heapq.heappush(speed_heap, speed)

            speed_sum += speed

            res = max(res, speed * efficiency)

        return res % ((10**9) + 7)
