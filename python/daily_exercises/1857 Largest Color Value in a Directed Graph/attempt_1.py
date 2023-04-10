import copy


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

        edge_dic = {}

        if len(edges) == 0:
            return 1

        def find_cycle(start_index):

            max_color = -1
            visited_set = set()

            stack = []
            color_array = [0 for _ in range(26)]
            stack.append((start_index, color_array, set()))

            while stack:

                node, color_array, seen_set = stack.pop()

                seen_set.add(node)
                visited_set.add(node)

                color_index = ord(colors[node]) - ord("a")
                color_array[color_index] += 1

                max_color = max(max_color, max(color_array))

                if node in edge_dic:
                    edges = edge_dic[node]

                    for edge in edges:
                        if edge in seen_set:
                            return -1, visited_set
                        else:
                            stack.append((edge, copy.deepcopy(color_array), copy.deepcopy(seen_set)))

            return max_color, visited_set

        num_set = set()
        for x, y in edges:

            if x not in edge_dic:
                edge_dic[x] = []
            edge_dic[x].append(y)

            num_set.add(x)
            num_set.add(y)

        res = -1
        start_num = 0

        while True:
            max_color, visited_set = find_cycle(start_num)

            if max_color == -1:
                return -1
            else:
                res = max(res, max_color)

                for visited_node in visited_set:
                    if visited_node in num_set:
                        num_set.remove(visited_node)

                if len(num_set) > 0:
                    start_num = num_set.pop()
                else:
                    return res
