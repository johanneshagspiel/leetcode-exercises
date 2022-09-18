import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:


        def clean_queue(index):

            if queue and queue[0] <= index - k:
                queue.popleft()

            while queue and nums[queue[-1]] < nums[index]:
                queue.pop()


        queue = collections.deque()

        solution = []

        max_index = 0

        n = len(nums)

        for index in range(k):
            clean_queue(index)
            queue.append(index)

            if nums[index] > nums[max_index]:
                max_index = index

        solution.append(nums[max_index])

        for index in range(k, n):
            clean_queue(index)
            queue.append(index)

            solution.append(nums[queue[0]])

        return solution