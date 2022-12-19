
class DUS:

    def __init__(self, n):
        self.root = [x for x in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def merge(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x == parent_y:
            return False

        else:
            rank_p_x = self.rank[parent_x]
            rank_p_y = self.rank[parent_y]

            if rank_p_x > rank_p_y:
                self.root[parent_y] = parent_x
                self.rank[parent_x] += self.rank[parent_y]

            elif rank_p_y > rank_p_x:
                self.root[parent_x] = parent_y
                self.rank[parent_y] += self.rank[parent_x]

            else:
                self.root[parent_y] = parent_x
                self.rank[parent_x] += self.rank[parent_y]

            return True

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        dus = DUS(n)

        for from_e, to_e in edges:
            dus.merge(from_e, to_e)

        return dus.find(source) == dus.find(destination)
