from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        N = len(nums)

        zero_c = 0
        one_c = 0
        two_c = 0

        for num in nums:
            if num == 0:
                zero_c += 1
            elif num == 1:
                one_c += 1
            elif num == 2:
                two_c += 1

        for i in range(N):
            cur_num = nums[i]

            if zero_c > 0:
                if cur_num != 0:
                    nums[i] = 0
                zero_c -= 1

            elif one_c > 0:
                if cur_num != 1:
                    nums[i] = 1
                one_c -= 1

            elif two_c > 0:
                if cur_num != 2:
                    nums[i] = 2
                two_c -= 1

        return nums
