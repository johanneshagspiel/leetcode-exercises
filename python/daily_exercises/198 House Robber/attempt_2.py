class Solution:
    def rob(self, nums: List[int]) -> int:
        num_houses = len(nums)

        if num_houses == 1:
            return nums[0]
        elif num_houses == 2:
            return max(nums[0], nums[1])

        next_two = nums[-1]
        next_one = max(nums[-2], nums[-1])

        for i in range(num_houses - 3, -1, -1):
            current = max(nums[i] + next_two, next_one)

            next_two = next_one
            next_one = current

        return next_one
