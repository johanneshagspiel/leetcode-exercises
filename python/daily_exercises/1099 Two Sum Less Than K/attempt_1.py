class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:

        nums.sort()
        left = 0
        right = len(nums) - 1
        max_sum = -1

        while left < right:
            num_left = nums[left]
            num_right = nums[right]

            combined_sum = num_left + num_right

            if combined_sum < k:
                max_sum = max(max_sum, combined_sum)
                left += 1
            else:
                right -= 1

        return max_sum
