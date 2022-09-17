class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        index_dic = {}

        for index, num in enumerate(nums):
            complement = target - num

            if complement in index_dic:
                return [index_dic[complement], index]
            else:
                index_dic[num] = index
