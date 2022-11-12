import heapq


class MedianFinder:

    def __init__(self):
        self.lower_max = []
        self.upper_min = []
        self.count = 0

    def addNum(self, num: int) -> None:

        heapq.heappush(self.lower_max, (-1) * num)

        to_add_upper = (-1) * heapq.heappop(self.lower_max)
        heapq.heappush(self.upper_min, to_add_upper)

        if len(self.lower_max) < len(self.upper_min):
            to_add_lower = (-1) * heapq.heappop(self.upper_min)
            heapq.heappush(self.lower_max, to_add_lower)

        self.count += 1

    def findMedian(self) -> float:

        if self.count % 2 == 1:
            return (-1) * self.lower_max[0]

        else:
            return (((-1) * self.lower_max[0]) + self.upper_min[0]) / 2
