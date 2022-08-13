class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.overlap = []


class MyCalendarTwo:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:

        if not self.root:
            self.root = Node(start, end - 1)
            return True

        else:
            return self._insert(self.root, start, end - 1)

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
            if len(node.overlap) == 0:
                node.overlap.append(Node(start, end))
                return True
            else:

                for overlap_node in node.overlap:

                    if overlap_node.start <= start <= overlap_node.end:
                        return False

                    if overlap_node.start <= end <= overlap_node.end:
                        return False

                    if start <= overlap_node.start and end >= overlap_node.end:
                        return False

                node.overlap.append(Node(start, end))
                return True
