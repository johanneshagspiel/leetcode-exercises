import heapq
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        priority_list = []
        priority_list.append((-1, nums[0]))

        for number in nums[1:]:
            not_found = True
            for count, compare_number in priority_list:
                if compare_number < number:
                    heapq.heappush(priority_list, ((count - 1), number))
                    not_found = False

            if not_found:
                heapq.heappush(priority_list, (-1, number))

        return (-1)*priority_list[0][0]