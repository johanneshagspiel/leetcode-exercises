class MyQueue:

    def __init__(self):
        self.stack = []

        self.left = 0
        self.right = 0

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.right += 1

    def pop(self) -> int:
        value = self.stack[self.left]
        self.left += 1
        return value

    def peek(self) -> int:
        return self.stack[self.left]

    def empty(self) -> bool:
        diff = self.right - self.left
        if diff == 0:
            return True
        else:
            return False

