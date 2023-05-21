class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        color = {}
        for vertex in range(len(graph)):
            if vertex not in color:
                color[vertex] = 0
                stack = [vertex]

                while stack:
                    node = stack.pop()

                    for nei in graph[node]:
                        if nei not in color:
                            color[nei] = color[node] ^ 1
                            stack.append(nei)
                        elif color[nei] == color[node]:
                            return False

        return True
