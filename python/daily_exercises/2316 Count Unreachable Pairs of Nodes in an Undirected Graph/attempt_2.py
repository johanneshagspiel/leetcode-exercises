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
                self.rank[rank_p_y] += 1
            else:
                self.parent[parent_y] = parent_x
                self.rank[parent_x] += 1

            return True


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        dus = DUS(n)

        for x, y in edges:
            dus.merge(x, y)

        node_size_dic = {}
        for num in range(n):
            parent = dus.find(num)

            if parent not in node_size_dic:
                node_size_dic[parent] = 0
            node_size_dic[parent] += 1

        numberOfPaths = 0
        remaining_nodes = n

        for nodeSize in node_size_dic.values():
            numberOfPaths += nodeSize * (remaining_nodes - nodeSize)
            remaining_nodes -= nodeSize

        return numberOfPaths
