class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):

        if k <= 1:
            return 0

        ans = left = 0
        prod = 1

        for right, value in enumerate(nums):

            prod *= value

            while prod >= k:
                prod /= nums[left]
                left += 1

            ans += right - left + 1

        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.numSubarrayProductLessThanK([1,2,3], 0))