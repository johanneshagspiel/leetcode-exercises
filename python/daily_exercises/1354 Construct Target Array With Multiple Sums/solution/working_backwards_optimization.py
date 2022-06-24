import heapq
from typing import List
class Solution:
    def isPossible(self, target: List[int]) -> bool:

        n = len(target)
        total_sum = sum(target)

        if n == 1:
            return target[0] == 1

        priority_list = [-x for x in target]
        heapq.heapify(priority_list)

        while -priority_list[0] > 1:

            largest = -priority_list[0]
            rest = total_sum - largest

            if rest == 1:
                return True

            x = largest % rest

            if x == 0 or x == largest:
                return False

            total_sum = total_sum - largest + x
            heapq.heapreplace(priority_list, -x)

        return True