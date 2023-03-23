
class DUS:

    def __init__(self, n):
        self.parent = [num for num in range(n)]
        self.rank = [0 for _ in range(n)]

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
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        if len(connections) < (n - 1):
            return - 1

        dus = DUS(n)
        num_connected_components = n

        for x, y in connections:
            parent_x = dus.find(x)
            parent_y = dus.find(y)

            if parent_x != parent_y:
                dus.merge(x, y)
                num_connected_components -= 1

        return num_connected_components - 1
