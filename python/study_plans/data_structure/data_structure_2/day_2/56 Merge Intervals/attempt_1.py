from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])

        merged = []
        merged.append(intervals[0])

        for cur_start, cur_end in intervals:

            prev_start = merged[-1][0]
            prev_end = merged[-1][1]

            if cur_start <= prev_end:
                merged.pop()
                max_end = max(cur_end, prev_end)

                merged.append((prev_start, max_end))
            else:
                merged.append((cur_start, cur_end))

        return merged