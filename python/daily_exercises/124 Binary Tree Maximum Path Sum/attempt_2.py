# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        max_sum = root.val

        def find_max_path(node):

            if not node:
                return 0

            nonlocal max_sum

            right_max_val = max(find_max_path(node.right), 0)
            left_max_val = max(find_max_path(node.left), 0)

            max_sum = max(max_sum, node.val + right_max_val + left_max_val)

            return max(node.val + left_max_val, node.val + right_max_val)

        find_max_path(root)
        return max_sum
