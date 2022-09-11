from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        n = len(prices)
        profit_list = []
        acc_profit = 0

        for position in range(1, n, 1):
            profit = prices[position] - prices[position - 1]

            if profit > 0:
                acc_profit += profit
            elif acc_profit != 0:
                profit_list.append(acc_profit)
                acc_profit = 0

        if acc_profit != 0:
            profit_list.append(acc_profit)

        profit_list.sort(reverse=True)
        res = sum(profit_list[:k])
        return res
