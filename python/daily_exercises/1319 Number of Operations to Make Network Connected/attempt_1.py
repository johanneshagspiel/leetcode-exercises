class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        node_set = set()
        cables = len(connections)

        for x, y in connections:
            node_set.add(x)
            node_set.add(y)

        needed_connections = n - len(node_set)

        if cables + 1 >= n:
            return needed_connections
        else:
            return -1
