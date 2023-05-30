
class Node():

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Bucket:
    def __init__(self):
        # a pseudo head
        self.head = Node(0)

    def insert(self, newValue):
        # if not existed, add the new element to the head.
        if not self.exists(newValue):
            newNode = Node(newValue, self.head.next)
            # set the new head.
            self.head.next = newNode

    def delete(self, value):
        prev = self.head
        curr = self.head.next
        while curr is not None:
            if curr.value == value:
                # remove the current node
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def exists(self, value):
        curr = self.head.next
        while curr is not None:
            if curr.value == value:
                # value existed already, do nothing
                return True
            curr = curr.next
        return False

class MyHashSet:

    def __init__(self):
        self.hash_key = 769
        self.bucket_list = [Bucket() for _ in range(self.hash_key)]

    def add(self, key: int) -> None:
        hash_key = self._determine_key(key)
        self.bucket_list[hash_key].insert(key)

    def remove(self, key: int) -> None:
        hash_key = self._determine_key(key)
        self.bucket_list[hash_key].delete(key)

    def contains(self, key: int) -> bool:
        hash_key = self._determine_key(key)
        return self.bucket_list[hash_key].exists(key)

    def _determine_key(self, key):
        return key % self.hash_key
