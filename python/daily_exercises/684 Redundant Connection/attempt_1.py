class DUS:

    def __init__(self, size):
        self.parent = []
        for number in range(size):
            self.parent.append(number)
        self.rank = [0 for _ in range(size)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x == parent_y:
            return False
        else:
            rank_px = self.rank[parent_x]
            rank_py = self.rank[parent_y]

            if rank_py > rank_px:
                self.parent[parent_x] = parent_y

            elif rank_px > rank_py:
                self.parent[parent_y] = parent_x

            else:
                self.parent[parent_x] = parent_y
                self.rank[rank_py] += 1

            return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        MAX_EDGE_SIZE = 1001
        res = None

        dus = DUS(MAX_EDGE_SIZE)

        for edge in edges:
            vertex_x = edge[0]
            vertex_y = edge[1]

            can_be_unionized = dus.union(vertex_x, vertex_y)

            if not can_be_unionized:
                res = edge

        return res
