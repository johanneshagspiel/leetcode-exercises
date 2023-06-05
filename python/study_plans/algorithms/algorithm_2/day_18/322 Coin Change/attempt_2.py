from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0

        coins.sort(reverse=True)

        remaining = amount
        coin_count = 0

        for coin in coins:

            amount_fit = remaining // coin

            if amount_fit > 0:
                coin_count += amount_fit
                remaining -= (amount_fit * coin)

                if remaining == 0:
                    return coin_count

        return -1

if __name__ == "__main__":
    print(2//3)

[1,2,5]
11
[2]
3
[1]
0