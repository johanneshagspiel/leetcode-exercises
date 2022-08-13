# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        parent = {}

        found_q = False
        found_p = False

        stack = []
        stack.append(root)

        while not found_p or not found_q:
            node = stack.pop()

            if node == p:
                found_p = True

            elif node == q:
                found_q = True

            if node.left:
                parent[node.left] = node
                stack.append(node.left)

            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        ancestor_q = set()

        while q:
            ancestor_q.add(q)

            if q in parent:
                q = parent[q]
            else:
                break

        while p:
            if p in ancestor_q:
                return p
            else:
                p = parent[p]

        return p
