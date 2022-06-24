class MaxStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:

        if len(self.stack) == 0:
            self.stack.append((x, x))
        else:
            current_max_value = self.stack[-1][1]
            if x > current_max_value:
                self.stack.append((x, x))
            else:
                self.stack.append((x, current_max_value))

    def pop(self) -> int:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return self.stack[-1][1]

    def popMax(self) -> int:
        max = self.stack[-1][1]

        to_push_list = []
        while self.stack[-1][0] != max:
            to_push_list.append(self.stack.pop())

        self.pop()
        to_push_list.reverse()
        map(lambda x: self.push(x), to_push_list)

        return max
