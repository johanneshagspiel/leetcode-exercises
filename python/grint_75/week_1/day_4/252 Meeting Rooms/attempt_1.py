from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        intervals.sort(key=lambda x: x[0])

        prev_end_time = None
        for index, (start_time, end_time) in enumerate(intervals):
            if index == 0:
                prev_end_time = end_time
            else:
                if start_time < prev_end_time:
                    return False
                else:
                    prev_end_time = end_time

        return True

if __name__ == '__main__':
    solution = Solution()
    matrix = [[7,10],[2,4]]
    output = solution.canAttendMeetings(matrix)
    print(output)