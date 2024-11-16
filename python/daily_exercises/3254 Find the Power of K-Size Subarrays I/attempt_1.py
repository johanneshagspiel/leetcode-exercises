import collections


class Solution(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        queue = collections.deque()

        for index in range(len(nums)):
            if queue and queue[0] < index - k + 1:
                queue.popleft()

            if queue and nums[index] != nums[index - 1] + 1:
                queue.clear()

            queue.append(index)

            if index >= k - 1:
                if len(queue) == k:
                    max_num = nums[queue[-1]]
                    res.append(max_num)
                else:
                    res.append(-1)

        return res
