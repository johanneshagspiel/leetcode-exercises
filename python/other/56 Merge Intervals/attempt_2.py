from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key= lambda x:x[1])

        N = len(intervals)
        skip_next = False
        last_to_check = False

        result_list = []

        for position in range(1, N):

            if skip_next:
                skip_next = False
                last_to_check = True

            else:
                previous_start, previous_end = intervals[position-1]
                current_start, current_end = intervals[position]

                max_start = max(previous_start, current_start)
                min_end = min(previous_end, current_end)

                if max_start <= min_end:
                    min_start = min(previous_start, current_start)
                    max_end = max(previous_end, current_end)

                    result_list.append((min_start, max_end))
                    skip_next = True
                    last_to_check = False

                else:
                    result_list.append((previous_start, previous_end))
                    last_to_check = True

        if last_to_check:
            result_list.append((intervals[-1][0], intervals[-1][1]))

        return result_list
