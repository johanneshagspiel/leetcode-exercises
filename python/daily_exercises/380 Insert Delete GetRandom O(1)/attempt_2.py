import random


class RandomizedSet:

    def __init__(self):
        self.dic = {}
        self.list = []

    def insert(self, val: int) -> bool:

        if val not in self.dic:
            self.dic[val] = len(self.list)
            self.list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:

        if val in self.dic:
            last_position_val = self.list[-1]
            delete_position = self.dic[val]

            self.list[delete_position] = last_position_val
            self.dic[last_position_val] = delete_position

            self.list.pop()
            del self.dic[val]

            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.list)

