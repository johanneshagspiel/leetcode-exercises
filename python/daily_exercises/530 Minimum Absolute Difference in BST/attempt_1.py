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

        val_list = []

        def in_order(node):

            if not node:
                return

            in_order(node.left)
            val_list.append(node.val)
            in_order(node.right)

        in_order(root)

        min_dif = float("inf")
        for i in range(1, len(val_list)):
            cur_abs_dif = abs(val_list[i-1] - val_list[i])
            min_dif = min(min_dif, cur_abs_dif)

        return min_dif
