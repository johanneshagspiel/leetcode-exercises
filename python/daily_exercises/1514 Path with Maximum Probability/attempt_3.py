import collections
import heapq


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:

        graph = {}

        for index, (from_node, to_node) in enumerate(edges):
            probability = succProb[index]

            if from_node not in graph:
                graph[from_node] = []
            if to_node not in graph:
                graph[to_node] = []

            graph[from_node].append((probability, to_node))
            graph[to_node].append((probability, from_node))

        max_prob = [0.0 for _ in range(n)]

        pq = [(-1.0, start)]

        while pq:
            cur_prob, cur_node = heapq.heappop(pq)

            if cur_node == end:
                return -cur_prob

            else:
                node_list = graph[cur_node]

                for next_prob, next_node in node_list:
                    if -cur_prob * next_prob > max_prob[next_node]:
                        max_prob[next_node] = -cur_prob * next_prob
                        heapq.heappush(pq, (-max_prob[next_node], next_node))

        return 0.0
