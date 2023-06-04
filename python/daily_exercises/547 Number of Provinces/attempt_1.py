import collections


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        graph = {}

        for city_id, adjacency_list in enumerate(isConnected): 
            graph[city_id] = []
            for neighbor_id, is_connected in enumerate(adjacency_list):
                if neighbor_id != city_id and is_connected:
                    graph[city_id].append(neighbor_id)

        visited = set()

        def dfs(city_id):
            queue = []
            queue.append(city_id)

            while queue:
                current_city_id = queue.pop()
                visited.add(current_city_id)

                neighbors = graph[current_city_id]
                for neighbor in neighbors:
                    if neighbor not in visited:
                        queue.append(neighbor)

        regions = 0
        for city_id, adjacency_list in graph.items():
            if city_id not in visited:
                regions += 1
                dfs(city_id)

        return regions
