# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        min_dif = float("inf")
        self.prev_val = None

        def in_order(node):

            nonlocal min_dif

            if not node:
                return

            in_order(node.left)

            if self.prev_val is not None:
                min_dif = min(min_dif, node.val - self.prev_val)

            self.prev_val = node.val

            in_order(node.right)

        in_order(root)

        return min_dif
