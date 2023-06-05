import operator
from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        pairs.sort(key= lambda x: x[0])

        N = len(pairs)
        dp = [0 for _ in range(N)]

        for i in range(1, N):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

