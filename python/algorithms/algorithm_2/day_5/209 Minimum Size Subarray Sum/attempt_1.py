import math
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        ans = math.inf
        len_nums = len(nums)
        running_sum = 0

        for right, value in enumerate(nums):

            running_sum += value

            if running_sum >= target:
                while running_sum >= target and left < len_nums:
                    running_sum -= nums[left]
                    left += 1

                if left == len_nums and running_sum >= target:
                    break

                elif left == len_nums:
                    left -= 1
                    running_sum += nums[left]

                    distance = right - left + 1
                    ans = min(ans, distance)

                else:
                    running_sum += nums[left]
                    left -= 1

                    distance = right - left + 1
                    ans = min(ans, distance)

        return 0 if ans == math.inf else ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.minSubArrayLen(4, [1,4,4]))