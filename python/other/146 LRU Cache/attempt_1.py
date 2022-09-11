import collections


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.recency_list = collections.deque()


    def get(self, key: int) -> int:
        if key in self.cache:
            self._make_key_most_recent(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if key not in self.cache:

            if self.capacity > 0:
                self.cache[key] = value
                self.capacity -= 1
                self.recency_list.append(key)

            else:
                least_recent_accessed = self.recency_list.popleft()
                self.cache.pop(least_recent_accessed)
                self.cache[key] = value
                self.recency_list.append(key)

        else:
            self.cache[key] = value
            self._make_key_most_recent(key)


    def _make_key_most_recent(self, key):

        new_recency_list = collections.deque()

        for element in self.recency_list:
            if element != key:
                new_recency_list.append(element)

        new_recency_list.append(key)

        self.recency_list = new_recency_list
