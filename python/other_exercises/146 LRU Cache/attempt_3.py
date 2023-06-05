class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.key_to_recency = {}
        self.recency_to_key = {}

        self.least_recent = 0
        self.most_recent = 0


    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        else:
            previous_recency = self.key_to_recency[key]
            self.recency_to_key.pop(previous_recency)

            self.recency_to_key[self.most_recent] = key
            self.key_to_recency[key] = self.most_recent

            self.most_recent += 1

            return self.cache[key]


    def put(self, key: int, value: int) -> None:

        if key not in self.cache:

            if self.capacity > 0:

                self.cache[key] = value
                self.recency_to_key[self.most_recent] = key
                self.key_to_recency[key] = self.most_recent

                self.most_recent += 1
                self.capacity -= 1

            else:

                while self.least_recent not in self.recency_to_key:
                    self.least_recent += 1

                least_recent_key = self.recency_to_key[self.least_recent]

                self.key_to_recency.pop(least_recent_key)
                self.recency_to_key.pop(self.least_recent)
                self.cache.pop(least_recent_key)

                self.least_recent += 1

                self.cache[key] = value
                self.recency_to_key[self.most_recent] = key
                self.key_to_recency[key] = self.most_recent

                self.most_recent += 1

        else:

            self.cache[key] = value

            previous_recency = self.key_to_recency[key]

            self.recency_to_key.pop(previous_recency)

            self.recency_to_key[self.most_recent] = key
            self.key_to_recency[key] = self.most_recent

            self.most_recent += 1
