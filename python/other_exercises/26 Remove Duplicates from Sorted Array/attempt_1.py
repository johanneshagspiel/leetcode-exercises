from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:


        insert_position = 1
        last_number = nums[0]

        N = len(nums)

        for index in range(1, N):

            cur_num = nums[index]

            if cur_num > last_number:
                nums[insert_position] = cur_num
                insert_position += 1
                last_number = cur_num

        return insert_position
