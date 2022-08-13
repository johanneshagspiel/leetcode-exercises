class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None


class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:

        if not self.root:
            self.root = Node(start, end-1)
            return True

        else:
            return self._insert(self.root, start, end-1)

    def _insert(self, node, start, end):

        if node.end < start:
            if node.right:
                return self._insert(node.right, start, end)
            else:
                node.right = Node(start, end)
                return True

        elif node.start > end:
            if node.left:
                return self._insert(node.left, start, end)
            else:
                node.left = Node(start, end)
                return True
        else:
            return False

