class Node:

    def __init__(self, key=-float("inf"), value=-float("inf")):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head


    def _remove(self, node):
        previous_node = node.prev
        next_node = node.next

        previous_node.next = next_node
        next_node.prev = previous_node

    def _add_to_head(self, node):
        next_node = self.head.next

        next_node.prev = node
        node.next = next_node

        self.head.next = node
        node.prev = self.head

    def _move_to_head(self, node):
        self._remove(node)
        self._add_to_head(node)

    def _remove_from_tail(self):
        least_recent_node = self.tail.prev
        self._remove(least_recent_node)
        return least_recent_node



    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self._move_to_head(node)
            return node.value


    def put(self, key: int, value: int) -> None:

        if key not in self.cache:
            node = Node(key=key, value=value)
            self._add_to_head(node)
            self.cache[key] = node
            self.capacity -= 1

            if self.capacity < 0:
                least_recent_node = self._remove_from_tail()
                self.cache.pop(least_recent_node.key)
                self.capacity += 1

        else:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
            self.cache[key] = node
