from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x:x[1])
        deleted = 0

        prev_start = intervals[0][0]
        prev_end = intervals[0][1]
        N = len(intervals)

        for index in range(1, N):

            cur_start = intervals[index][0]
            cur_end = intervals[index][1]

            if prev_end > cur_start:
                deleted += 1
            else:
                prev_start = cur_start
                prev_end = cur_end

        return deleted


