from typing import List


class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:

        neighbourhoods = 0
        previous_neighbourhood = -1

        for house in houses:
            if house == 0:
                previous_neighbourhood = -1
            else:
                if house != previous_neighbourhood:
                    neighbourhoods += 1

        if neighbourhoods > target:
            return -1

        else:
            dp = [[[0]*target for _ in range(n)] for _ in range(m)]