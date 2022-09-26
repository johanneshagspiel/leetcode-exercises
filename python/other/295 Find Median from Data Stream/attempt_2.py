class MedianFinder:

    def __init__(self):
        self.lower_max_heap = []
        self.upper_min_heap = []
        self.count = 0

    def addNum(self, num: int) -> None:

        heapq.heappush(self.lower_max_heap, -num)

        to_add = (-1) * heapq.heappop(self.lower_max_heap)
        heapq.heappush(self.upper_min_heap, to_add)

        if len(self.lower_max_heap) < len(self.upper_min_heap):
            to_add = (-1) * heapq.heappop(self.upper_min_heap)
            heapq.heappush(self.lower_max_heap, to_add)

        self.count += 1

    def findMedian(self) -> float:

        if self.count % 2 == 1:
            return - self.lower_max_heap[0]

        else:
            return (self.upper_min_heap[0] - self.lower_max_heap[0]) / 2
