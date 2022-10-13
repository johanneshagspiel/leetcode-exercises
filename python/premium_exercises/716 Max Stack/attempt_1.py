import heapq


class MaxStack:

    def __init__(self):
        self.stack = []
        self.heap = []

        self.cnt = 0
        self.removed = set()

    def push(self, x: int) -> None:
        heapq.heappush(self.heap, (-x, -self.cnt))
        self.stack.append((x, self.cnt))
        self.cnt += 1


    def pop(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()

        value, index = self.stack.pop()
        self.removed.add(index)
        return value


    def top(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()
        return self.stack[-1][0]


    def peekMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.removed:
            heapq.heappop(self.heap)
        return -self.heap[0][0]


    def popMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.removed:
            heapq.heappop(self.heap)

        value, index = heapq.heappop(self.heap)
        self.removed.add(-index)
        return -value
