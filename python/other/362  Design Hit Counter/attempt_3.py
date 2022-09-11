import collections


class HitCounter:

    def __init__(self):
        self.linked_list = collections.deque()
        self.total = 0

    def hit(self, timestamp: int) -> None:

        if len(self.linked_list) == 0:
            self.linked_list.append((1, timestamp))

        else:
            last_timestamp = self.linked_list[-1][1]

            if last_timestamp == timestamp:
                count, timestamp = self.linked_list.pop()
                self.linked_list.append((count + 1, timestamp))

            else:
                self.linked_list.append((1, timestamp))

        self.total += 1


    def getHits(self, timestamp: int) -> int:

        start_not_found = True

        while start_not_found:

            if len(self.linked_list) > 0:
                first_timestamp = self.linked_list[0][1]
                difference = timestamp - first_timestamp

                if difference >= 300:
                    count, timestamp = self.linked_list.popleft()
                    self.total -= count
                else:
                    start_not_found = False
            else:
                start_not_found = False

        return self.total
