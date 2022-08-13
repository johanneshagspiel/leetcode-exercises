import heapq


class MyCalendar:

    def __init__(self):
        self.interval_list = []

    def book(self, start: int, end: int) -> bool:

        for prev_end, prev_start in self.interval_list:
            if prev_start <= start <= prev_end:
                return False

            if prev_start <= end-1 <= prev_end:
                return False

            if start <= prev_start and end-1 >= prev_end:
                return False

        heapq.heappush(self.interval_list, (end-1, start))
        return True

