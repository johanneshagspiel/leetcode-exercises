class Node:

    def __init__(self, value=None, key=None):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None


class LRUCache:

    def _add_node(self, node):
        next_node = self.head.next

        self.head.next = node
        node.prev = self.head

        node.next = next_node
        next_node.prev = node

    def _remove_node(self, node):
        next_node = node.next
        prev_node = node.prev

        next_node.prev = prev_node
        prev_node.next = next_node

    def _pop_tail(self):
        res = self.tail.prev
        self._remove_node(res)
        return res

    def move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)


    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:

        if key in self.cache:
            node = self.cache[key]
            self.move_to_head(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = Node(key=key, value=value)
            self.cache[key] = node
            self._add_node(node)
            self.capacity -= 1

            if self.capacity < 0:
                res = self._pop_tail()
                self.cache.pop(res.key)

        else:
            node = self.cache[key]
            node.value = value
            self.cache[key] = node
            self.move_to_head(node)
