from typing import List


class Solution:
    def minSwaps(self, data: List[int]) -> int:

        left = right = 0
        cnt_ones = max_ones = 0
        window_size = sum(data)

        while right < len(data):
            cnt_ones += data[right]
            right += 1

            if right - left > window_size:
                cnt_ones -= data[left]
                left += 1
                max_ones = max(max_ones, cnt_ones)

        return window_size - max_ones
