
class Disjoin_Union_Set:

    def __init__(self, n):
        self.parent = [x for x in range(n)]
        self.rank = [x for x in range(n)]

    def find(self, x):
        parent_x = self.parent[x]

        if x != parent_x:
            self.parent[x] = self.find(parent_x)

        return self.parent[x]

    def merge(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x == parent_y:
            return False
        else:
            rank_x = self.rank[parent_x]
            rank_y = self.rank[parent_y]

            if rank_x > rank_y:
                self.parent[parent_y] = parent_x
                self.rank[parent_x] += 1
            elif rank_y > rank_x:
                self.parent[parent_x] = parent_y
                self.rank[parent_y] += 1
            else:
                self.parent[parent_y] = parent_x
                self.rank[parent_x] += 1

            return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connectedComponent = n
        dus = Disjoin_Union_Set(n)

        for x, y in edges:
            merged = dus.merge(x, y)
            if merged:
                connectedComponent -= 1

        return connectedComponent

