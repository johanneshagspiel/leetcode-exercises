from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        N = len(intervals)
        if N == 1:
            return intervals

        intervals.sort(key=lambda x: (x[1], x[0]))
        result_list = []

        skip_now = False

        for position in range(1, N):
            current_start, current_end = intervals[position]

            if skip_now:
                skip_now = False

            else:

                previous_start, previous_end = intervals[position-1]

                min_start = min(previous_start, current_start)
                max_end = max(previous_end, current_end)

                if min_start <= max_end:
                    result_list.append((min_start, max_end))
                else:
                    result_list.append((previous_start, previous_end))
                    result_list.append((current_start, current_end))

        return result_list