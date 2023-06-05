class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.pop(0)

    def peek(self) -> int:
        first_entry = self.queue[0]
        return first_entry

    def empty(self) -> bool:
        return len(self.queue) == 0

if __name__ == '__main__':
    queue = MyQueue()

    queue.push(1)
    print(queue)

    queue.push(2)
    print(queue)

    print(queue.peek())

    print(queue.pop())

    print(queue.empty())