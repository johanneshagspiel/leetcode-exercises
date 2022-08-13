# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()

            if node.val > p.val and node.val > q.val:
                stack.append(node.left)

            elif node.val < p.val and node.val < q.val:
                stack.append(node.right)

            else:
                return node

