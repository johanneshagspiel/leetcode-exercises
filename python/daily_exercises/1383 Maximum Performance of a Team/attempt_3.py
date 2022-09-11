import heapq
from typing import List


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:

        tuple_list = sorted(list(zip(efficiency, speed)), reverse=True)

        speed_acc = 0
        max_performance = 0
        speed_list = []

        for efficiency, speed in tuple_list:

            if len(speed_list) > (k - 1):
                speed_acc -= heapq.heappop(speed_list)

            speed_acc += speed
            heapq.heappush(speed_list, speed)

            max_performance = max(max_performance, speed_acc * efficiency)

        return max_performance % ((10**9) + 7)

