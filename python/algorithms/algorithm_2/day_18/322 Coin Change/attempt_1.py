import math
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        self.min_coin = math.inf

        def back_track(remaining, coin_count):

            if remaining == 0:
                self.min_coin = min(coin_count, self.min_coin)
                return

            elif remaining < 0:
                return

            else:

                for coin in coins:
                    remaining -= coin
                    coin_count += 1

                    back_track(remaining, coin_count)

                    remaining += coin
                    coin_count -= 1

        back_track(amount, 0)

        return -1 if self.min_coin == math.inf else self.min_coin



