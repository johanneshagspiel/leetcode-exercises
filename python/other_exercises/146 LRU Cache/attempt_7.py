
class LinkedNode:

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.head = LinkedNode()
        self.tail = LinkedNode()

        self.head.next = self.tail
        self.tail.prev = self.head


    def move_to_head(self, node):
        self.remove_node(node)
        self.add_to_head(node)


    def add_to_head(self, node):
        next_head = self.head.next

        self.head.next = node
        node.prev = self.head

        node.next = next_head
        next_head.prev = node


    def remove_node(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node


    def pop_tail(self):
        prev_tail = self.tail.prev
        self.remove_node(prev_tail)
        return prev_tail



    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self.move_to_head(node)
            return node.value


    def put(self, key: int, value: int) -> None:

        if key not in self.cache:
            node = LinkedNode(key=key, value=value)
            self.add_to_head(node)
            self.cache[key] = node
            self.capacity -= 1

            if self.capacity < 0:
                prev_tail = self.pop_tail()
                self.cache.pop(prev_tail.key)

        else:
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)
            self.cache[key] = node
