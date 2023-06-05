class MyQueue:

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []
        self.front = None

    def push(self, x: int) -> None:

        if len(self.stack_1) == 0:
            self.front = x

        self.stack_1.append(x)


    def pop(self) -> int:

        if len(self.stack_2) == 0:
            for element in range(len(self.stack_1)):
                self.stack_2.append(self.stack_1.pop())

        return self.stack_2.pop()


    def peek(self) -> int:

        if len(self.stack_2) != 0:
            return self.stack_2[0]
        else:
            return self.front


    def empty(self) -> bool:
        return (len(self.stack_1) == 0) and (len(self.stack_2) == 0)


if __name__ == "__main__":

    myQueue = MyQueue()
    print(myQueue.push(1)) # queue is: [1]
    print(myQueue.push(2)) # queue is: [1, 2](leftmost is front of the queue)
    print(myQueue.peek()) # return 1
    print(myQueue.pop()) # return 1, queue is [2]
    print(myQueue.empty()) # return false