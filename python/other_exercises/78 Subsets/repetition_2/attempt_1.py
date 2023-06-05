from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result_list = []
        N = len(nums)

        def back_tracking(subset_size, current_list, start_index):

            if len(current_list) == subset_size:
                result_list.append(current_list)
                return

            elif start_index >= N:
                return

            else:

                for index in range(start_index, N):
                    current_list.append(nums[index])
                    back_tracking(subset_size, current_list, index + 1)
                    current_list.pop()


        for subset_size in range(N):
            back_tracking(0, [], 0)

        return result_list



