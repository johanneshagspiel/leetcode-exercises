class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left_ones = 0
        right_ones = 0
        max_con_ones = 0

        for num in nums:
            if num == 1:
                right_ones += 1
            else:
                cur_comb = left_ones + right_ones
                max_con_ones = max(max_con_ones, cur_comb)
                left_ones = right_ones + 1
                right_ones = 0

        max_con_ones = max(max_con_ones, left_ones + right_ones)
        return max_con_ones