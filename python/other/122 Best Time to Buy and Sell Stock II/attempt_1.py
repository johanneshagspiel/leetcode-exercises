class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        N = len(prices)

        res = 0

        for i in range(1, N):
            dif = prices[i] - prices[i-1]
            if dif > 0:
                res += dif

        return res
