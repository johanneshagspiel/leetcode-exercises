import math


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((val, val))
        else:
            prev_min_val = self.stack[-1][1]
            if val < prev_min_val:
                self.stack.append((val, val))
            else:
                self.stack.append((val, prev_min_val))

    def pop(self) -> None:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

