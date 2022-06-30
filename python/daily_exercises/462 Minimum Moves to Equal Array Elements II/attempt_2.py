from typing import List
class Solution:
    def minMoves2(self, nums: List[int]) -> int:

        smallest = min(nums)
        largest = max(nums)
        distance = largest - smallest + 1

        dp = [0 for _ in range(distance)]
        index = 0

        for compare_number in range(smallest, largest+1):
            for num in nums:
                addition = 0
                if num > compare_number:
                    addition = num - compare_number
                elif num < compare_number:
                    addition = compare_number - num

                dp[index] += addition
            index += 1

        return min(dp)
