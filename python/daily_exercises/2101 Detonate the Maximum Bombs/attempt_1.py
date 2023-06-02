import math

class DUS():

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x != parent_y:
            self.parent[y] = parent_x
            self.rank[parent_x] += 1

    def get_max_rank(self):
        return max(self.rank)


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        n = len(bombs)

        dus = DUS(n)

        for i in range(n):
            x1, y1, r1 = bombs[i]

            for j in range(i + 1, n):
                x2, y2, r2 = bombs[j]

                x_distance = x2 - x1
                y_distance = y2 - y1

                distance = math.sqrt(pow(x_distance, 2) + pow(y_distance, 2))

                if distance <= r1:
                    dus.merge(i, j)

        return dus.get_max_rank()
