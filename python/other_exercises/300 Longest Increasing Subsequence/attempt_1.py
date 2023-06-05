from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        res = [float("inf")]

        for num in nums:

            M = len(res)
            prev = float("inf")
            for position in range(M):
                smal = res[position]

                if smal > num and num > prev:
                    res[position] = num
                    if position == (M - 1):
                        res.append(float("inf"))
                    break
                else:
                    prev = smal

        return len(res) - 1


