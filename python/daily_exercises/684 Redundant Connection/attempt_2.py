from typing import List

class DS:

    def __init__(self, size):
        self.rank = [0 for _ in range(size)]
        self.parent = []

        for number in range(size):
            self.parent.append(number)

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

            if rank_px > rank_py:
                self.parent[parent_y] = parent_x

            elif rank_py > rank_px:
                self.parent[parent_x] = parent_y

            else:
                self.parent[parent_y] = parent_x
                self.rank[parent_x] += 1

            return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        redundant_edge = None
        ds = DS(1001)

        for edge in edges:
            vert_1 = edge[0]
            vert_2 = edge[1]

            redundant = ds.union(vert_1, vert_2)

            if not redundant:
                redundant_edge = edge

        return redundant_edge
