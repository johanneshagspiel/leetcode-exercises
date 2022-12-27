class Solution:
    def canJump(self, nums: List[int]) -> bool:

        reachable_list = [False for _ in range(len(nums))]
        reachable_list[-1] = True

        for index in range(len(nums) -2, -1, -1):
            max_position = min(index + nums[index] + 1, len(nums))
            reachable_list[index] = any(reachable_list[index + 1 : max_position])

        return reachable_list[0]
