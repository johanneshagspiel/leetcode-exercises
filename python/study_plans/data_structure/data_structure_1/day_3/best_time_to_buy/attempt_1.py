from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        current_cheapeast_buy = 99999999999999999999999999999

        for index, price in enumerate(prices):
            if index == 0:
                current_cheapeast_buy = price
            else:
                current_profit = price - current_cheapeast_buy

                if current_profit > max_profit:
                    max_profit = current_profit

                if price < current_cheapeast_buy:
                    current_cheapeast_buy = price

        return max_profit

if __name__ == '__main__':
    solution = Solution()

    input_1 = [7,1,5,3,6,4]
    output_1 = solution.maxProfit(input_1)
    expected_output = 5
    print(output_1)
