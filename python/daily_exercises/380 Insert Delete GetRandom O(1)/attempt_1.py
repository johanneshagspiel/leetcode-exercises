import random


class Bucket:

    def __init__(self):
        self.content = []

    def add(self, val):
        self.content.append(val)

    def _find_index(self, val):
        found_index = -1

        for index, num in enumerate(self.content):
            if num == val:
                found_index = index
                break

        return found_index

    def delete(self, val):

        found_index = self._find_index(val)

        if found_index == -1:
            return False
        else:
            self.content.pop(found_index)
            return True

    def exists(self, val):

        found_index = self._find_index(val)

        if found_index == -1:
            return False
        else:
            return True


class Hash_Set:
    def __init__(self):
        self.hash_space = 2059
        self.buckets = [Bucket() for _ in range(self.hash_space)]

    def _hash(self, val):
        return val % self.hash_space

    def insert(self, val: int) -> bool:
        hash_key = self._hash(val)
        self.buckets[hash_key].add(val)

    def remove(self, val: int) -> bool:
        hash_key = self._hash(val)
        return self.buckets[hash_key].delete(val)

    def exists(self, val):
        hash_key = self._hash(val)
        return self.buckets[hash_key].exists(val)


class RandomizedSet:

    def __init__(self):
        self.element_set = Hash_Set()
        self.element_list = []
        self.overwrite_set = Hash_Set()

    def insert(self, val: int) -> bool:

        exists = self.element_set.exists(val)

        if exists:
            return False

        else:
            self.element_set.insert(val)
            self.overwrite_set.remove(val)
            self.element_list.append(val)
            return True

    def remove(self, val: int) -> bool:
        exists = self.element_set.remove(val)

        if exists:
            self.overwrite_set.insert(val)

        return exists

    def getRandom(self) -> int:

        not_found = True

        while not_found:
            rand_pos = random.randint(0, len(self.element_list)-1)
            rand_val = self.element_list[rand_pos]

            if not self.overwrite_set.exists(rand_val):
                not_found = False

        return rand_val

