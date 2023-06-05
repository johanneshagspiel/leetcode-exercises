class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        N = len(nums)
        res = [1 for _ in range(N)]

        for position in range(1, N):
            res[position] = nums[position-1] * res[position - 1]

        right = 1

        for position in range(N-2, -1, -1):
            right = right * nums[position+1]
            res[position] = res[position] * right

        return res
