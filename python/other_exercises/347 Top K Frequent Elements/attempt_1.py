import collections
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = collections.Counter(nums)

        priority_list = []

        for num, count in counter.items():

            heapq.heappush(priority_list, (-count, num))

        res = heapq.nsmallest(k, priority_list)

        return [x[1] for x in res]

