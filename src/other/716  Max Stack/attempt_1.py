import math
from collections import deque

class MaxStack:

    def __init__(self):
        self.stack = []
        self._max_value = -math.inf
        self._max_value_index = None

    def push(self, x: int) -> None:
        self.stack.append(x)

        if x >= self._max_value:
            self._max_value = x
            self._max_value_index = len(self.stack) - 1

    def pop(self) -> int:
        top_value = self.stack.pop()

        if self._max_value_index == 0:
            self._find_new_max_value()
        else:
            self._max_value_index -= 1

        return top_value

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.stack[self._max_value_index]

    def popMax(self) -> int:
        max_value = self.stack.pop(self._max_value_index)
        self._find_new_max_value()
        return max_value

    def _find_new_max_value(self):

        if len(self.stack) == 0:
            self._max_value = math.inf
            self._max_value_index = None

        else:
            new_max_val = -math.inf
            new_max_index = None

            for index, value in enumerate(self.stack):
                if value > new_max_val:
                    new_max_val = value
                    new_max_index = index

            self._max_value = new_max_val
            self._max_value_index = new_max_index
