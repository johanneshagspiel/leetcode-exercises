import math
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        self.main_count = math.inf
        coins.sort(reverse=True)

        def back_tracking(remaining, coin_count):

            if remaining == 0:
                self.main_count = min(self.main_count, coin_count)
                return

            elif remaining < 0:
                return

            else:

                for coin_value in coins:

                    amount_fit = remaining // coin_value

                    if amount_fit > 0:

                        for coin_amount in range(amount_fit, -1, -1):
                            remaining -= (coin_amount * coin_value)
                            coin_count += coin_amount

                            back_tracking(remaining, coin_count)

                            remaining += (coin_amount * coin_value)
                            coin_count -= coin_amount

        back_tracking(amount, 0)

        return self.main_count if self.main_count != math.inf else -1
