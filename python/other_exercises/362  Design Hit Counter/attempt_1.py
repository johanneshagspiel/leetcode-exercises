class HitCounter:

    def __init__(self):
        self.hit_dic = {}

    def hit(self, timestamp: int) -> None:
        prev_res = self.hit_dic.get(timestamp, 0)
        self.hit_dic[timestamp] = (prev_res + 1)

    def getHits(self, timestamp: int) -> int:

        end = max(timestamp - 300, 0)
        total = 0

        for second in range(timestamp, end, -1):
            if second in self.hit_dic:
                total += self.hit_dic[second]

        return total
            