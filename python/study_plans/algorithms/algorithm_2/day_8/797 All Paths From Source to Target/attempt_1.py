import copy
from typing import List
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        stack = []
        stack.append((0, [0]))
        result_list = []
        n = len(graph) - 1

        while stack:
            current_node, current_path = stack.pop()

            if current_node == n:
                result_list.append(current_path)
            else:
                possible_options = graph[current_node]

                for option in possible_options:
                    new_path = copy.deepcopy(current_path)
                    new_path.append(option)
                    stack.append((option, new_path))

        return result_list

