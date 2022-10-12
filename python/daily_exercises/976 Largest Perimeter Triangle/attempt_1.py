class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        if len(nums) < 3:
            return 0

        nums.sort(reverse=True)

        for c_p in range(len(nums) - 2):
            c = nums[c_p]
            b = nums[c_p + 1]
            a = nums[c_p + 2]

            if b + a > c:
                return a + b + c

        return 0
