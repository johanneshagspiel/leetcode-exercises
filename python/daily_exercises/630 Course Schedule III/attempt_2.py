import heapq
from typing import List
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:

        priority_queue = []
        courses.sort(key=lambda x:x[1])

        # first_duration, first_last_day = courses.pop(0)
        # heapq.heappush(priority_queue, (-first_duration))
        # current_time = first_duration

        current_time = 0

        for duration, last_day in courses:
            if current_time + duration <= last_day:
                current_time = current_time + duration
                heapq.heappush(priority_queue, (-duration))
            else:
                if len(priority_queue) > 0:
                    longest_duration = priority_queue[0] * -1

                    if longest_duration > duration:
                        heapq.heappop(priority_queue)
                        heapq.heappush(priority_queue, ( -duration))
                        current_time = current_time - longest_duration + duration

        return len(priority_queue)
