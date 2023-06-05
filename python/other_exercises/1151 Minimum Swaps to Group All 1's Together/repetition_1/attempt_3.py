from typing import List


class Solution:
    def minSwaps(self, data: List[int]) -> int:

        left = right = 0
        max_ones = count_ones = 0
        window_size = sum(data)

        while right < len(data):
            count_ones += data[right]
            right += 1

            if right - left > window_size:
                count_ones -= data[left]
                left += 1

            max_ones = max(max_ones,count_ones)

        return window_size- max_ones
    