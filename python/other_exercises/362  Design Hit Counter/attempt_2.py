import collections


class HitCounter:

    def __init__(self):
        self.hit_dic = {}

    def hit(self, timestamp: int) -> None:

        if timestamp not in self.hit_dic:
            self.hit_dic[timestamp] = 0

        self.hit_dic[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        start = max(0, timestamp-300)

        count = 0

        for second in range(start, timestamp+1):
            if second in self.hit_dic:
                count += self.hit_dic[second]

        return count


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)