import collections


class Solution:
    def reverseWords(self, s: str) -> str:
        overall_dequeue = collections.deque()

        current_dequeue = collections.deque()

        for char in s:
            if char.isspace():
                if len(current_dequeue) > 0:
                    current_string = "".join(current_dequeue)
                    overall_dequeue.appendleft(current_string)
                    current_dequeue = collections.deque()
            else:
                current_dequeue.append(char)

        if len(current_dequeue) > 0:
            current_string = "".join(current_dequeue)
            overall_dequeue.appendleft(current_string)

        return " ".join(overall_dequeue)