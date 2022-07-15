from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        total_sum = sum(matchsticks)
        return total_sum % 4 == 0