
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        visited = set()

        def dfs(city_id):
            queue = []
            queue.append(city_id)

            while queue:
                current_city_id = queue.pop()
                visited.add(current_city_id)

                adjacency_list = isConnected[current_city_id]
                for neighbor_id, is_connected in enumerate(adjacency_list):
                    if neighbor_id != city_id and neighbor_id not in visited and is_connected:
                        queue.append(neighbor_id)

        regions = 0
        for city_id in range(len(isConnected)):
            if city_id not in visited:
                regions += 1
                dfs(city_id)

        return regions
