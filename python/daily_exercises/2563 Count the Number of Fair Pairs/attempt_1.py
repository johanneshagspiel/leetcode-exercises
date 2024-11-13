import bisect


class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """

        def binary_search(list, target, lower_b, upper_b):
            while lower_b <= upper_b:
                mid = lower_b + ((upper_b - lower_b) // 2)
                pivot = list[mid]

                if pivot >= target:
                    upper_b = mid -1
                else:
                    lower_b = mid + 1

            return lower_b

        nums.sort()
        res = 0

        for i in range(len(nums)):
            current_num = nums[i]

            f_lower = binary_search(nums, lower - current_num, i + 1, len(nums) - 1)
            f_upper = binary_search(nums, upper - current_num + 1, i + 1, len(nums) - 1)

            res += f_upper - f_lower

        return res
