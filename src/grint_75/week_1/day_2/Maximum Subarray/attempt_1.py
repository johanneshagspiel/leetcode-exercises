import math
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_profit = -math.inf
        cur_profit_rolling = -math.inf

        for number in nums:
            cur_profit_rolling = max(number, cur_profit_rolling + number)
            max_profit = max(max_profit, cur_profit_rolling)

        return max_profit


if __name__ == '__main__':
    solution = Solution()

    nums = [-2,1,-3,4,-1,2,1,-5,4]
    output_1 = solution.maxSubArray(nums)
    expected_output = 6
    print(output_1)
