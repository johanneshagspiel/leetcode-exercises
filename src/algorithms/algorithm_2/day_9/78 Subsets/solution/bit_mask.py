from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        result_list = []

        for index in range(2**n, 2**(n-1)):
            bitmask = bin(index)[3:]
            result_list.append([nums[j] for j in range(n) if bitmask[j] == '1'])

        return result_list
