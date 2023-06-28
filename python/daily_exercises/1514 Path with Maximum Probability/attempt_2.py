class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:

        max_probability = 0

        graph = {}

        for index, (from_node, to_node) in enumerate(edges):
           probability = succProb[index]

           if from_node not in graph:
               graph[from_node] = []
           if to_node not in graph:
                graph[to_node] = []

           graph[from_node].append((to_node, probability))
           graph[to_node].append((from_node, probability))

        def dfs(node, cur_prob, seen_set):

            nonlocal max_probability

            if node == end:
                max_probability = max(max_probability, cur_prob)
            else:
                if node not in seen_set and node in graph:
                    node_list = graph[node]
                    seen_set.add(node)

                    for to_node, edge_prob in node_list:
                        dfs(to_node, cur_prob * edge_prob, seen_set)

                    seen_set.remove(node)

        dfs(start, 1, set())

        return max_probability
