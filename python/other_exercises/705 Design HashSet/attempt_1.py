class Bucket:

    def __init__(self):
        self.content = []


    def add(self, key):
        not_found = True

        for value in self.content:
            if value == key:
                not_found = False

        if not_found:
            self.content.append(key)


    def remove(self, key):
        found_index = -1

        for index, value in enumerate(self.content):
            if value == key:
                found_index = index
                break

        if found_index != -1:
            self.content.pop(found_index)


    def contains(self, key):
        found_index = -1

        for index, value in enumerate(self.content):
            if value == key:
                found_index = index
                break

        if found_index != -1:
            return True
        else:
            return False


class MyHashSet:

    def __init__(self):
        self.key_space = 2096
        self.hash_list = [Bucket() for _ in range(self.key_space)]

    def add(self, key: int) -> None:
        hash_key = key % self.key_space
        self.hash_list[hash_key].add(key)


    def remove(self, key: int) -> None:
        hash_key = key % self.key_space
        self.hash_list[hash_key].remove(key)


    def contains(self, key: int) -> bool:
        hash_key = key % self.key_space
        return self.hash_list[hash_key].contains(key)
