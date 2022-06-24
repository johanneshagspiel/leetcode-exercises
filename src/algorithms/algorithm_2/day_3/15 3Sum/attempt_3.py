from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        duplicates = set()
        results = set()
        seen_dic = {}

        for index_1, value_1 in enumerate(nums):
            if value_1 not in duplicates:
                duplicates.add(value_1)

                for index_2, value_2 in enumerate(nums[index_1+1:]):
                    complement = 0 - value_1 - value_2

                    if complement in seen_dic and seen_dic[complement] == index_1:
                        results.add(sorted(tuple(value_1, value_2, complement)))

                    seen_dic[value_2] = index_1

        return results
