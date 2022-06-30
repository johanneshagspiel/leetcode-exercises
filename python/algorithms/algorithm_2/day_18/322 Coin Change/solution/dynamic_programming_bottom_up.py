import math
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [math.inf for _ in range(amount + 1)]
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)

        result = dp[-1]
        return result if result != math.inf else -1
