import random


class RandomizedSet:

    def __init__(self):
        self.dic = {}
        self.key_list = []
        self.count = 0

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        else:
            self.dic[val] = self.count
            self.key_list.append(val)
            self.count += 1
            return True

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False
        else:
            to_delete_index = self.dic[val]
            last_val = self.key_list[-1]

            self.dic[last_val] = to_delete_index
            self.key_list[-1] = val
            self.key_list[to_delete_index] = last_val

            self.key_list.pop()
            self.dic.pop(val)
            self.count -= 1

            return True

    def getRandom(self) -> int:
        random_index = random.randint(0, self.count - 1)
        random_val = self.key_list[random_index]

        return random_val
