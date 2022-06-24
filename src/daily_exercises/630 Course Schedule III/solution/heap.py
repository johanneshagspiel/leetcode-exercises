import heapq
from typing import List
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:

        priority_queue = []

        courses.sort(key=lambda x:x[1])
        start_time = 0

        for duration, end_day in courses:
            if start_time + duration <= end_day:
                heapq.heappush(priority_queue, (-1* duration))
                start_time = start_time + duration
            else:
                if len(priority_queue) > 0:
                    longest_duration = -1 * priority_queue[0]
                    if longest_duration > duration:
                        heapq.heappop(priority_queue)
                        heapq.heappush(priority_queue, (-1 * duration))
                        start_time = start_time - longest_duration + duration

        return len(priority_queue)