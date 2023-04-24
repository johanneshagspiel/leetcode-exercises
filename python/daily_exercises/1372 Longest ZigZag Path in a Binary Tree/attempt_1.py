# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        def zig_zag(root, go_left):

            moves = -1

            stack = []
            stack.append(root)

            while stack:

                node = stack.pop()
                moves += 1

                if go_left:
                    if node.left:
                        stack.append(node.left)
                        go_left = False
                else:
                    if node.right:
                        stack.append(node.right)
                        go_left = True

            return moves

        if not root:
            return 0

        else:

            zig = zig_zag(root, True)
            zag = zig_zag(root, False)

            return max(zig, zag, 0)