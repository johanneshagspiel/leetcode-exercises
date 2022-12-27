class Solution:
    def canJump(self, nums: List[int]) -> bool:

        last_reachable_position = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            max_position = nums[i]

            if i + max_position >= last_reachable_position:
                last_reachable_position = i

        return last_reachable_position == 0