class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0], reverse=False)

        max_interval = 0
        current_inverval = 0

        initial_start = -1
        initial_end = -1

        overlap_stack = [(initial_start, initial_end)]

        for start, end in intervals:

            previous_start, previous_end = overlap_stack.pop()

            max_start = max(previous_start, start)
            min_end = min(previous_end, end)

            if max_start <= min_end:


            else:
                max_interval = max(current_inverval, max_interval)
                current_inverval = 0

                current_start = start
                current_end = end

        return max_interval
