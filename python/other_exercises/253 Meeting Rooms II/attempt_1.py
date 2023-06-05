import heapq
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        intervals.sort(key= lambda x: x[0])

        room_list = []

        for start, end in intervals:

            if len(room_list) == 0:
                room_list.append(end)

            else:
                if room_list[0] <= start:
                    heapq.heappushpop(room_list, end)
                else:
                    heapq.heappush(room_list, end)

        return len(room_list)

