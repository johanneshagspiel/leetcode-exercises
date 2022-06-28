from typing import List
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        n = len(cardPoints)
        window_size = n - k

        total_sum = sum(cardPoints)
        max_sum = 0

        for start_index in range(n-k):
            sub_array = cardPoints[start_index:(start_index+window_size)]
            cur_remainder = sum(sub_array)
            cur_sum = total_sum - cur_remainder

            if cur_sum > max_sum:
                max_sum = cur_sum


        for end_index in range(n, n-k, -1):
            sub_array = cardPoints[(end_index-window_size):end_index]
            cur_remainder = sum(sub_array)
            cur_sum = total_sum - cur_remainder

            if cur_sum > max_sum:
                max_sum = cur_sum
        
        return max_sum
