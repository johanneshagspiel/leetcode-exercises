import collections


class Solution(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        index_queue = collections.deque()
        res = []

        for index in range(len(nums)):
            if len(index_queue) > 0 and index_queue[0] < index - k + 1:
                index_queue.popleft()

            if len(index_queue) > 0 and nums[index] != nums[index - 1] + 1:
                index_queue.clear()

            index_queue.append(index)

            if index >= k - 1:
                if len(index_queue) == k:
                    res.append(nums[index])
                else:
                    res.append(-1)

        return res
