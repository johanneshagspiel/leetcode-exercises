# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        max_dif = -float("inf")
        stack = [(root, root.val, root.val)]

        while stack:
            node, max_ancestor_val, min_ancestor_val = stack.pop()

            cur_dif_max = abs(max_ancestor_val - node.val)
            max_dif = max(max_dif, cur_dif_max)
            cur_dif_min = abs(min_ancestor_val - node.val)
            max_dif = max(max_dif, cur_dif_min)

            max_ancestor_val = max(max_ancestor_val, node.val)
            min_ancestor_val = min(min_ancestor_val, node.val)

            if node.right:
                stack.append((node.right, max_ancestor_val, min_ancestor_val))
            if node.left:
                stack.append((node.left, max_ancestor_val, min_ancestor_val))

        return max_dif
