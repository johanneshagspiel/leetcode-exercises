import collections
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_counter = collections.Counter(nums)

        priority_list = []

        for num, count in num_counter.items():
            heapq.heappush(priority_list, (-count, num))

        most_frequent = heapq.nsmallest(k, priority_list)

        return [x[1] for x in most_frequent]

