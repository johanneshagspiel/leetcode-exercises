
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []



class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        if not node:
            return node

        seen_node_dic = {}

        def safe_clone_graph(node):

            if node.val not in seen_node_dic:

                new_node = Node()
                new_node.val = node.val
                seen_node_dic[node.val] = new_node

                for neighbor_node in node.neighbors:
                    new_neighbor_node = safe_clone_graph(neighbor_node)
                    new_node.neighbors.append(new_neighbor_node)

                return new_node

            else:
                return seen_node_dic[node.val]

        return safe_clone_graph(node)
