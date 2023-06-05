from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        n = len(graph) - 1
        result_list = []

        def back_track(node, path):

            if node == n:
                result_list.append(list(path))
                return

            else:
                for connected_node in graph[node]:
                    path.append(connected_node)
                    back_track(connected_node, path)
                    path.pop()

        path = [0]
        back_track(0, path)
        return result_list