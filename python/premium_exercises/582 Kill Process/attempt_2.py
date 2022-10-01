class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:

        parent_to_node_dic = collections.defaultdict(list)

        for node, parent in zip(pid, ppid):
            parent_to_node_dic[parent].append(node)

        stack = []
        ans = [kill]

        stack.extend(parent_to_node_dic[kill])
        ans.extend(parent_to_node_dic[kill])
        del parent_to_node_dic[kill]

        while stack:
            node = stack.pop()

            if node in parent_to_node_dic:
                stack.extend(parent_to_node_dic[node])
                ans.extend(parent_to_node_dic[node])
                del parent_to_node_dic[node]

        return ans
