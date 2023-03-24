class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        reachable = set()
        reachable.add(0)

        reorders = 0

        while connections:

            new_connections = connections

            for index, connection in enumerate(new_connections):
                x, y = connection

                if x in reachable:
                    reorders += 1
                    reachable.add(y)
                    connections.pop(index)
                elif y in reachable:
                    reachable.add(x)
                    connections.pop(index)

        return reorders
