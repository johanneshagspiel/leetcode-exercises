class MedianFinder:

    def __init__(self):
        self.max_lower_heap = []
        self.min_upper_heap = []
        self.count = 0

    def addNum(self, num: int) -> None:

        heapq.heappush(self.max_lower_heap, - num)

        to_add_number = (-1) * heapq.heappop(self.max_lower_heap)
        heapq.heappush(self.min_upper_heap, to_add_number)

        if len(self.max_lower_heap) < len(self.min_upper_heap):
            to_add_number = (-1) * heapq.heappop(self.min_upper_heap)
            heapq.heappush(self.max_lower_heap, to_add_number)

        self.count += 1

    def findMedian(self) -> float:

        if self.count % 2 == 1:
            return -self.max_lower_heap[0]
        else:
            return (self.min_upper_heap[0] - self.max_lower_heap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()