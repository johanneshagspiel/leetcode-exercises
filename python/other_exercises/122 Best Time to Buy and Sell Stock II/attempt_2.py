from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0
        N = len(prices)

        for i in range(1, N):
            dif = prices[i] - prices[i-1]

            if dif > 0:
                res += dif

        return res
        