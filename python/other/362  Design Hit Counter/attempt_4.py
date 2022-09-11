import collections


class HitCounter:

    def __init__(self):
        self.linked_list = collections.deque()
        self.size = 0

    def hit(self, timestamp: int) -> None:

        if len(self.linked_list) == 0:
            self.linked_list.append((timestamp, 1))

        else:
            last_timestamp = self.linked_list[-1][0]

            if last_timestamp == timestamp:
                last_count, last_timestamp = self.linked_list.pop()
                last_count += 1
                self.linked_list.append((last_count, last_timestamp))
            else:
                self.linked_list.append((timestamp, 1))

        self.size += 1

    def getHits(self, timestamp: int) -> int:

        not_found = True

        while not_found:

            if len(self.linked_list) > 0:

                first_timestamp = self.linked_list[0][0]
                difference = timestamp - first_timestamp

                if difference >= 300:
                    timestamp, count = self.linked_list.popleft()
                    self.size -= count
                else:
                    not_found = False

            else:
                not_found = False

        return self.size
