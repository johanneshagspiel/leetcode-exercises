import math
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def rec_mem(remaining, mem_dic):

            if remaining == 0:
                return 0

            elif remaining < 0:
                return math.inf

            elif remaining in mem_dic:
                return mem_dic[remaining]

            else:

                result_list = []
                for coin in coins:
                    result_list.append(1 + rec_mem(remaining - coin, mem_dic))

                result = min(result_list)
                mem_dic[remaining] = result
                return result

        result =  rec_mem(amount, {})

        return result if result != math.inf else -1
