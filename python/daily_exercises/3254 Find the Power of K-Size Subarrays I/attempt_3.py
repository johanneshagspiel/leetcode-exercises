import collections


class Solution(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        cons_count = 0
        res = []

        for index in range(len(nums)):
            if cons_count == k:
                cons_count -= 1

            if cons_count != 0 and nums[index] != nums[index - 1] + 1:
                cons_count = 0

            cons_count += 1

            if index >= k - 1:
                if cons_count == k:
                    res.append(nums[index])
                else:
                    res.append(-1)

        return res
