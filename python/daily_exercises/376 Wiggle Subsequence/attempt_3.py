from typing import List
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:

        n = len(nums)
        compare_number = nums[0]
        count = 1
        mode = 0

        for num in nums[1:]:
            if mode == 0:
                if num > compare_number:
                    count += 1
                    compare_number = nums
                    mode = 1

            elif mode == 1:
                if num < compare_number:
                    count += 1
                    compare_number = nums
                    mode = 0

        max_mode_0 = count

        compare_number = nums[0]
        count = 1
        mode = 1

        for num in nums[1:]:
            if mode == 0:
                if num > compare_number:
                    count += 1
                    compare_number = nums
                    mode = 1

            elif mode == 1:
                if num < compare_number:
                    count += 1
                    compare_number = nums
                    mode = 0

        max_mode_1 = count

        max_0 = max(max_mode_0, max_mode_1)


        compare_number = nums[1]
        count = 1
        mode = 0

        for num in nums[2:]:
            if mode == 0:
                if num > compare_number:
                    count += 1
                    compare_number = nums
                    mode = 1

            elif mode == 1:
                if num < compare_number:
                    count += 1
                    compare_number = nums
                    mode = 0

        max_mode_0 = count

        compare_number = nums[1]
        count = 1
        mode = 1

        for num in nums[2:]:
            if mode == 0:
                if num > compare_number:
                    count += 1
                    compare_number = nums
                    mode = 1

            elif mode == 1:
                if num < compare_number:
                    count += 1
                    compare_number = nums
                    mode = 0

        max_mode_1 = count

        max_1 = max(max_mode_0, max_mode_1)

        return max(max_0, max_1)