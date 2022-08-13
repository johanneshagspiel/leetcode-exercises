from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result_list = []
        N = len(nums)

        def two_sum(target, nums):

            dic = {}
            result_list = []

            for num in nums:
                complement = target - num
                if complement in dic:
                    result_list.append([complement, num])

                dic[complement] = True

            return result_list


        for index, num in enumerate(nums):
            temp_result_list = two_sum(0 - num, nums[index:])
            if len(temp_result_list) > 0:
                for res1, res2 in temp_result_list:
                    result_list.append((num, res1, res2))

        return result_list

