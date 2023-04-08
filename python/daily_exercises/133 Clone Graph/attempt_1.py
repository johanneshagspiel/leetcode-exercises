
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
        connected_node_dic = {}

        def safe_clone_graph(node):

            if node.val not in seen_node_dic:

                new_node = Node()
                new_node.val = node.val
                seen_node_dic[node.val] = new_node

                for neighbor_node in node.neighbors:
                    safe_clone_graph(neighbor_node)

                return new_node

        def connect_nodes(node):

            if node.val in connected_node_dic:
                return connected_node_dic[node.val]
            else:
                new_node = seen_node_dic[node.val]

                for neighbor_node in node.neighbors:
                    new_neighbor_node = seen_node_dic[neighbor_node.val]
                    new_node.neighbors.append(new_neighbor_node)

                connected_node_dic[node.val] = new_node

                for neighbor_node in node.neighbors:
                    _ = connect_nodes(neighbor_node)

                return new_node


        safe_clone_graph(node)
        return connect_nodes(node)
