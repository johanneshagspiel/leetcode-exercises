import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        def clean_queue(index):

            if queue and queue[0] <= index - k:
                queue.popleft()

            while queue and nums[index] > nums[queue[-1]]:
                queue.pop()


        queue = collections.deque()

        n = len(nums)

        max_index = 0

        res = []

        for index in range(k):
            clean_queue(index)
            queue.append(index)

            if nums[index] > nums[max_index]:
                max_index = index

        res.append(nums[max_index])

        for index in range(k, n):
            clean_queue(index)
            queue.append(index)

            res.append(nums[queue[0]])

        return res
