import json
from typing import List
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        n = len(cardPoints)
        rest = n - k
        total_sum = sum(cardPoints)
        max_sum = 0

        for start_index in range(rest -1, -1, -1):
            sub_array = cardPoints[start_index:(start_index + rest)]
            cur_sum = total_sum - sum(sub_array)
            if cur_sum > max_sum:
                max_sum = cur_sum

        return max_sum