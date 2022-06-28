from typing import List
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        start_index = 0
        current_sum = 0
        n = len(cardPoints)
        rest = n - k
        total_score = sum(cardPoints)
        min_sum = total_score

        if k == n:
            return total_score

        for i in range(n):
            current_sum += cardPoints[i]
            curr_len = i - start_index + 1

            if curr_len == rest:
                min_sum = min(min_sum, current_sum)
                current_sum -= cardPoints[start_index]
                start_index += 1

        return total_score - min_sum
