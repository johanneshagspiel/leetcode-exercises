class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:

        total_sum = sum(nums)

        left_sum = 0
        left_average = 0

        min_average = float("inf")
        min_ind = -1

        for i, num in enumerate(nums):
            left_sum += num
            left_average = int(left_sum / (i + 1))

            if i == (len(nums) - 1):
                right_average = 0
            else:
                right_sum = total_sum - left_sum
                right_average = int(right_sum / (len(nums) - i - 1))

            abs_dif = abs(left_average - right_average)

            if abs_dif < min_average:
                min_average = abs_dif
                min_ind = i

        return min_ind
