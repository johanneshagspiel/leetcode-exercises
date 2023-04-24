# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        max_path = 0

        def zig_zag(node, go_left):

            nonlocal max_path

            if not node:
                return -1

            else:
                go_left_options = 1 + zig_zag(node.left, False)
                go_right_options = 1 + zig_zag(node.right, True)

                max_path = max(max_path, go_left_options, go_right_options)

                if go_left:
                    final_options = go_left_options
                else:
                    final_options = go_right_options

                return final_options

        _ = zig_zag(root, True)

        return max_path
