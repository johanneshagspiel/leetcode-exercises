class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.entry_to_recency = {}
        self.recency_to_entry = {}

        self.least_recent = 0
        self.most_recent = 0


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            previous_recency = self.entry_to_recency[key]
            self.entry_to_recency[key] = self.most_recent

            self.recency_to_entry.pop(previous_recency)
            self.recency_to_entry[self.most_recent] = key

            self.most_recent += 1

            return self.cache[key]


    def put(self, key: int, value: int) -> None:

        if key not in self.cache:
            if self.capacity > 0:
                self.cache[key] = value

                self.entry_to_recency[key] = self.most_recent
                self.recency_to_entry[self.most_recent] = key

                self.most_recent += 1
                self.capacity -= 1

            else:

                while self.least_recent not in self.recency_to_entry:
                    self.least_recent += 1

                least_recent_entry = self.recency_to_entry[self.least_recent]
                self.recency_to_entry.pop(self.least_recent)
                self.cache.pop(least_recent_entry)
                self.entry_to_recency.pop(least_recent_entry)
                self.least_recent += 1

                self.cache[key] = value
                self.entry_to_recency[key] = self.most_recent
                self.recency_to_entry[self.most_recent] = key
                self.most_recent += 1

        else:
            previous_recency = self.entry_to_recency[key]
            self.entry_to_recency[key] = self.most_recent

            self.recency_to_entry.pop(previous_recency)
            self.recency_to_entry[self.most_recent] = key

            self.cache[key] = value

            self.most_recent += 1
