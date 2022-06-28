from typing import List
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        start_index = 0
        cur_sum = 0
        n = len(cardPoints)
        req_len = n -k

        total_sum = sum(cardPoints)
        min_sum = total_sum

        if n == k:
            return total_sum

        for index in range(n):
            cur_sum += cardPoints[index]
            cur_len = index - start_index + 1

            if cur_len == req_len:
                min_sum = min(min_sum, cur_sum)
                cur_sum -= cardPoints[start_index]
                start_index += 1

        return total_sum - min_sum
