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
                self.rank[parent_x] += self.rank[parent_y]
            elif rank_p_y > rank_p_x:
                self.parent[parent_x] = parent_y
                self.rank[parent_y] += self.rank[parent_x]
            else:
                self.parent[parent_y] = parent_x
                self.rank[parent_x] += self.rank[parent_y]

            return True


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        dus = DUS(n)

        for x, y in edges:
            dus.merge(x, y)
            dus.find(x)
            dus.find(y)

        added_set = set()
        node_size_list = []

        for parent in dus.parent:
            prev_parent = -1
            parent = dus.find(parent)
            while parent != prev_parent:
                prev_parent = parent
                parent = dus.find(parent)

            if parent not in added_set:
                node_size = dus.rank[parent] + 1
                node_size_list.append(node_size)
                added_set.add(parent)

        existing_nodes = len(node_size_list)
        cum_sum = [0 for _ in range(existing_nodes)]

        cum_sum[-1] = node_size_list[-1]

        for i in range(existing_nodes-1, -1, -1):
            cum_sum[i] = node_size_list[i] + cum_sum[i - 1]

        result = 0
        for i in range(existing_nodes - 1):
            result += node_size_list[i] * cum_sum[i + 1]

        return result
