import math

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        graph = collections.defaultdict(list)
        n = len(bombs)

        for i in range(n):
            xi, yi, ri, = bombs[i]

            for j in range(n):
                if i == j:
                    continue

                xj, yj, rj, = bombs[j]

                x_distance = xi - xj
                y_distance = yi - yj

                distance = math.sqrt(pow(x_distance, 2) + pow(y_distance, 2))

                if ri >= distance:
                    graph[i].append(j)

        def dfs(current, visited):
            visited.add(current)

            for nei in graph[current]:
                if nei not in visited:
                    dfs(nei, visited)
            return len(visited)

        answer = 0
        for i in range(n):
            visited = set()
            answer = max(answer, dfs(i, visited))

        return answer
