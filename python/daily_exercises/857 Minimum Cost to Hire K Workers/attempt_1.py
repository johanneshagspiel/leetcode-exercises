from typing import List


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:

        fraction_list = sorted([(wage / quality, quality, wage) for quality, wage in zip(quality, wage)], reverse=True)
        return fraction_list
