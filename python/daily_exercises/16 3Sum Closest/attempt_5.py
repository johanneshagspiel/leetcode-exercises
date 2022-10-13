class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        n = len(nums)
        min_diff = float("inf")

        nums.sort()

        for i in range(n):
            low = i + 1
            high = n - 1

            while low < high:
                sum = nums[i] + nums[low] + nums[high]

                if abs(target - sum) < abs(min_diff):
                    min_diff = target - sum

                if abs(sum) < abs(target):
                    low += 1

                else:
                    high -= 1

            if min_diff == 0:
                return target

        return target - min_diff

