from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        for start_point, end_point in intervals:
            print(start_point)

if __name__ == "__main__":
    solution = Solution()

    intervals = [[0,30],[5,10],[15,20]]
    output = solution.canAttendMeetings(intervals)
    print(output)


