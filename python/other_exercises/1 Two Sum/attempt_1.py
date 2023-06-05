from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic = {}

        for index, num in enumerate(nums):
            complement = target - num

            if complement in dic:
                other_ind = dic[complement]
                return (index, other_ind)

            else:
                dic[num] = index
