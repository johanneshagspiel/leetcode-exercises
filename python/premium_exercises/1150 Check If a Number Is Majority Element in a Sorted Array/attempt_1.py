class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:

        num_count = 0

        target_count = (len(nums) // 2) + 1

        for num in nums:

            if num == target:
                num_count += 1

            if num_count == target_count:
                return True

        return False
