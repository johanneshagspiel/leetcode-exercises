from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:

        nums.sort()

        leftVal = nums[0]
        right = len(nums) - 1

        while right > 0:
            rightVal = nums[right]

            sumVal = leftVal + rightVal

            if sumVal <= target:
                break
            else:
                right -= 1

        sum = 0

        while left < right:
            dif = right - left

        return sum

class Main:

    if __name__ == "__main__":

        nums = [7, 6, 5, 3]
        target = 9

        test = Solution()
        res = test.numSubseq(nums, target)
        print(res)
