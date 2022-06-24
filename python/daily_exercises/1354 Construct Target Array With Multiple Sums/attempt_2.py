import heapq
from typing import List
class Solution:
    def isPossible(self, target: List[int]) -> bool:

        n = len(target)

        if n ==1:
            return target == [1]

        total_sum = sum(target)

        priority_list = [(-1)*x for x in target]
        heapq.heapify(priority_list)

        while priority_list[0] < -1:

            largest = priority_list[0]*(-1)

            rest_sum = total_sum - largest

            if rest_sum == 1:
                return True
            
            if rest_sum >= largest:
                return False

            x = largest % rest_sum

            total_sum = total_sum - largest + x

            heapq.heapreplace(priority_list, -x)

        return True