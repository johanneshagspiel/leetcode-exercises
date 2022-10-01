class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:

        parent_to_node_dic = collections.defaultdict(list)

        for node, parent in zip(pid, ppid):
            parent_to_node_dic[parent].append(node)

        answer = []
        answer.append(kill)

        if kill in parent_to_node_dic:

            stack = parent_to_node_dic[kill]

            del parent_to_node_dic[kill]
            answer.extend(stack)

            while stack:

                node = stack.pop()

                if node in parent_to_node_dic:
                    children = parent_to_node_dic[node]
                    del parent_to_node_dic[node]

                    answer.extend(children)
                    stack.extend(children)

        return answer
