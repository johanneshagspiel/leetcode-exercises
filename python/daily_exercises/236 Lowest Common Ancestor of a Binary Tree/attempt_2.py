# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(start_node, target):
            stack = []
            stack.append((start_node, [start_node]))

            while stack:
                node, path = stack.pop()

                if node == target:
                    return path
                else:
                    if node.left:
                        new_path = path[:]
                        new_path.append(node.left)
                        stack.append((node.left, new_path))
                    if node.right:
                        new_path = path[:]
                        new_path.append(node.right)
                        stack.append((node.right, new_path))

        path_q = dfs(root, q)
        path_p = dfs(root, p)

        q_len = len(path_q)
        p_len = len(path_p)

        min_len = q_len if q_len < p_len else p_len
        prev_node = root

        for position in range(1, min_len+1):
            q_node = path_q[position]
            p_node = path_p[position]

            if q_node != p_node:
                return prev_node
            else:
                prev_node = q_node

        return prev_node
