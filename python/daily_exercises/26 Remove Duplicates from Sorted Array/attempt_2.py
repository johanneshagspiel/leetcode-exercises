class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insertIndex = 1
        size = len(nums)

        for i in range(1, size):
            if nums[i] != nums[i-1]:
                nums[insertIndex] = nums[i]
                insertIndex += 1

        return insertIndex