class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        if source == destination:
            return True

        connection_dic = collections.defaultdict(list)

        for from_e, to_e in edges:
            connection_dic[from_e].append(to_e)
            connection_dic[to_e].append(from_e)

        stack = [source]
        seen = set()

        while stack:
            vertex = stack.pop()
            seen.add(vertex)

            if vertex == destination:
                return True
            else:
                targets = connection_dic[vertex]

                for target in targets:
                    if target not in seen:
                        stack.append(target)

        return False
