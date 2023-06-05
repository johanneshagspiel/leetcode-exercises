import heapq


class MedianFinder:

    def __init__(self):
        self.lower_half = []
        self.upper_half = []
        self.count = 0

    def addNum(self, num: int) -> None:

        heapq.heappush(self.lower_half, -num)

        lower_half_largest_num = (-1) * heapq.heappop(self.lower_half)
        heapq.heappush(self.upper_half, lower_half_largest_num)

        if len(self.lower_half) < len(self.upper_half):
            upper_half_smallest_num = (-1) * heapq.heappop(self.upper_half)
            heapq.heappush(self.lower_half, upper_half_smallest_num)

        self.count += 1

    def findMedian(self) -> float:

        if self.count % 2 == 0:
            return (self.upper_half[0] - self.lower_half[0]) / 2

        else:
            return - self.lower_half[0]
