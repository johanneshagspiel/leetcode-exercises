from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        chepeast_buy_price = 99999999999999999999999999999999

        for index, price in enumerate(prices):

            if index == 0:
                chepeast_buy_price = price

            else:
                profit = price - chepeast_buy_price

                if profit > max_profit:
                    max_profit = profit

                if price < chepeast_buy_price:
                    chepeast_buy_price = price

        return max_profit


if __name__ == '__main__':
    solution = Solution()

    input_1 = [0, 6, -3, 7]
    output_1 = solution.maxProfit(input_1)
    expected_output = 5
    print(output_1)
