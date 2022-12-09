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
        stack = [(root, [root.val])]

        while stack:
            node, ancestor_val_list = stack.pop()

            for ancestor_val in ancestor_val_list:
                cur_dif = abs(ancestor_val - node.val)
                max_dif = max(max_dif, cur_dif)

            ancestor_val_list.append(node.val)

            if node.right:
                stack.append((node.right, ancestor_val_list.copy()))
            if node.left:
                stack.append((node.left, ancestor_val_list.copy()))

        return max_dif


