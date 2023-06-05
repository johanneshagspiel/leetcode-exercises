from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result_set = set()
        len_nums = len(nums)

        def back_track(int_list, index):

            if int_list not in result_set:
                result_set.add(str(int_list))

            int_list = int_list.append(nums[index + 1])
            back_track(int_list, index + 1)
            int_list.pop()

        back_track([], 0)
        result_list = list(result_set)

        return result_list

