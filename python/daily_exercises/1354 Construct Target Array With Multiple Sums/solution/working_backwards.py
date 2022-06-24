import heapq
from typing import List
class Solution:
    def isPossible(self, target: List[int]) -> bool:

        total_sum = sum(target)

        priority_list = [-x for x in target]
        heapq.heapify(priority_list)

        while priority_list[0] < -1:

            largest = -priority_list[0]
            rest = total_sum - largest
            x = largest - rest

            if x < 1:
                return False

            total_sum = total_sum - largest + x

            heapq.heapreplace(priority_list, -x)

        return True