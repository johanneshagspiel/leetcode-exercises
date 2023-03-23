
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

        dus = DUS(n)
        redundant_connections = 0
        total_num_set = set([num for num in range(n)])
        last_element = 0

        for x, y in connections:
            con_exists = dus.merge(x, y)
            if con_exists:
                redundant_connections += 1

            if x in total_num_set:
                total_num_set.remove(x)
            if y in total_num_set:
                total_num_set.remove(y)
            last_element = x

        needed_connections = 0
        if len(total_num_set) > redundant_connections:
            return -1
        else:
            for num in total_num_set:
                merged = dus.merge(last_element, num)
                if merged:
                    needed_connections += 1

        return needed_connections
