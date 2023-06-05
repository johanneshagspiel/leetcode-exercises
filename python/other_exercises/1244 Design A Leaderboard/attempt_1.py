import heapq


class Leaderboard:

    def __init__(self):
        self.entry_dic = {}

    def addScore(self, playerId: int, score: int) -> None:

        if playerId in self.entry_dic:
            prev_val = self.entry_dic[playerId]
            score = prev_val + score
        self.entry_dic[playerId] = score

    def top(self, K: int) -> int:
        scores = list(map(lambda x: (-1)*x, self.entry_dic.keys()))
        return heapq.nlargest(K, scores)

    def reset(self, playerId: int) -> None:
        self.entry_dic[playerId] = 0

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)