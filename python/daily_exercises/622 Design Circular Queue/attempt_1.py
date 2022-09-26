class LinkedNode:

    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None


class MyCircularQueue:

    def __init__(self, k: int):
        self.head = LinkedNode()
        self.tail = LinkedNode()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = k
        self.entries = k

    def _remove_node(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def _pop_head(self):
        next_node = self.head.next
        self._remove_node(next_node)

    def _add_to_tail(self, node):
        prev_node = self.tail.prev

        self.tail.prev = node
        node.next = self.tail

        node.prev = prev_node
        prev_node.next = node

    def enQueue(self, value: int) -> bool:

        if self.isFull():
            return False

        else:
            new_node = LinkedNode(value=value)
            self._add_to_tail(new_node)
            self.entries -= 1
            return True

    def deQueue(self) -> bool:

        if self.isEmpty():
            return False

        else:
            self._pop_head()
            self.entries += 1
            return True

    def Front(self) -> int:

        if self.isEmpty():
            return -1
        else:
            return self.head.next.value

    def Rear(self) -> int:

        if self.isEmpty():
            return -1
        else:
            return self.tail.prev.value

    def isEmpty(self) -> bool:
        return self.size == self.entries

    def isFull(self) -> bool:
        return self.entries == 0

