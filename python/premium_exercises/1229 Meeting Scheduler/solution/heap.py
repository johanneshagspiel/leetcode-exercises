import heapq
from typing import List
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:

        priority_queue = []

        for start_time, end_time in slots1:
            temp_duration = end_time - start_time
            if temp_duration >= duration:
                heapq.heappush(priority_queue, (start_time, end_time))

        for start_time, end_time in slots2:
            temp_duration = end_time - start_time
            if temp_duration >= duration:
                heapq.heappush(priority_queue, (start_time, end_time))

        while priority_queue:

            current_start_time, current_end_time = heapq.heappop(priority_queue)

            if len(priority_queue) > 0:
                next_start_time, next_end_time = priority_queue[0]

                temp_duration = current_end_time - next_start_time

                if temp_duration >= duration:
                    return [next_start_time, next_start_time + duration]

        return []
