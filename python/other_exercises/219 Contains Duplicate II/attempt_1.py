from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        dic = set()

        for index, num in enumerate(nums):

            if num in dic:
                return True
            dic.add(num)
            if len(dic) > k:
                dic.remove(nums[index - k])

        return False
