class DUS:

    def __init__(self, n):
        self.parent = [num for num in range(n + 1)]
        self.rank = [0 for _ in range(n + 1)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def merge(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x == parent_y:
            return False
        else:
            rank_p_x = self.rank[parent_x]
            rank_p_y = self.rank[parent_y]

            if rank_p_x > rank_p_y:
                self.parent[parent_y] = parent_x
                self.rank[parent_x] += 1
            elif rank_p_y > rank_p_x:
                self.parent[parent_x] = parent_y
                self.rank[parent_y] += 1
            else:
                self.parent[parent_y] = parent_x
                self.rank[parent_x] += 1

            return True

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        dus = DUS(n)
        min_distance = float('inf')

        for x, y, distance in roads:
            dus.merge(x, y)

        parent_1 = dus.find(1)
        for x, y, distance in roads:
            parent_x = dus.find(x)
            if parent_x == parent_1:
                min_distance = min(min_distance, distance)
            else:
                parent_y = dus.find(y)
                if parent_y == parent_1:
                    min_distance = min(min_distance, distance)

        return min_distance