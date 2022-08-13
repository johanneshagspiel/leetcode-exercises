import heapq
from bisect import bisect_right


class MyCalendar:

    def __init__(self):
        self.interval_list = []

    def book(self, start: int, end: int) -> bool:

        id = bisect_right(self.interval_list, (start, end))

        if (id > 0 and self.interval_list[id-1][1] > start) or (id < len(self.interval_list) and self.interval_list[id][0] < end):
            return False

        heapq.heappush(self.interval_list, (start, end))
        return True