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

        stack = [(start, 1, set())]

        while stack:
            node, cur_prob, seen_set = stack.pop()

            if node == end:
                max_probability = max(max_probability, cur_prob)
            else:
                if node not in seen_set:
                    node_list = graph[node]
                    seen_set.add(node)

                    for to_node, edge_prob in node_list:
                        stack.append((to_node, cur_prob * edge_prob, seen_set))

        return max_probability

