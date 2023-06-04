class DUS:

    def __init__(self, n):
        self.parent = [x for x in range(n)]
        self.rank = [0 for x in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x != parent_y:
            rank_p_x = self.rank[parent_x]
            rank_p_y = self.rank[parent_y]

            if rank_p_y > rank_p_x:
                self.parent[parent_x] = parent_y
                self.rank[parent_y] += 1
            else:
                self.parent[parent_y] = parent_x
                self.rank[parent_x] += 1

            return True
        else:
            return False

    def get_regions(self):
        return len(set(self.parent))


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)
        dus = DUS(n)
        regions = n

        for city_id, adjacency_list in enumerate(isConnected):
            for neighbor_id, is_connected in enumerate(adjacency_list):
                if city_id != neighbor_id and is_connected:
                    merged = dus.merge(city_id, neighbor_id)
                    if merged:
                        regions -= 1

        return regions
