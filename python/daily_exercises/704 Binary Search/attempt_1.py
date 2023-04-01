class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + ((right - left) // 2)
            val_mid = nums[mid]

            if val_mid == target:
                return mid
            elif val_mid > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1