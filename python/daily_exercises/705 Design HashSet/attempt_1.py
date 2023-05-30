class MyHashSet:

    def __init__(self):
        self.hash_key = pow(10, 6)
        self.key_list = [False for _ in range(self.hash_key)]

    def add(self, key: int) -> None:
        hash_key = self._determine_key(key)
        self.key_list[hash_key] = True

    def remove(self, key: int) -> None:
        hash_key = self._determine_key(key)
        self.key_list[hash_key] = False

    def contains(self, key: int) -> bool:
        hash_key = self._determine_key(key)
        return self.key_list[hash_key]

    def _determine_key(self, key):
        return key % self.hash_key

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
