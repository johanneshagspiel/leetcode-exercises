class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0]*k
        self.head = 0

        self.count = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:

        if self.isFull():
            return False
        else:
            self.queue[(self.head + self.count) % self.capacity] = value
            self.count += 1
            return True

    def deQueue(self) -> bool:

        if self.isEmpty():
            return False
        else:
            self.head = (self.head + 1) % self.capacity
            self.count -= 1
            return True

    def Front(self) -> int:

        if self.isEmpty():
            return -1
        else:
            return self.queue[self.head]

    def Rear(self) -> int:

        if self.isEmpty():
            return -1
        else:
            return self.queue[(self.head + self.count - 1) % self.capacity]


    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity
