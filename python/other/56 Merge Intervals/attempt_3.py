from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        N = len(intervals)

        if N == 1:
            return intervals

        intervals.sort(key=lambda x:x[1])
        position = 1

        prev_start = intervals[0][0]
        prev_end = intervals[0][1]

        result_list = []

        while position < N:
            current_start = intervals[position][0]
            current_end = intervals[position][1]

            max_start = max(prev_start, current_start)
            min_end = min(prev_end, current_end)

            if max_start <= min_end:
                prev_start = min(prev_start, current_start)
                prev_end = max(prev_end, current_end)

            else:
                result_list.append((prev_start, prev_end))

                prev_start = current_start
                prev_end = current_end

            position += 1

        result_list.append((prev_start, prev_end))
        return result_list

