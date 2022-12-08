# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def get_leaf_sequence(root):

            res = ""
            stack = [root]

            while stack:

                node = stack.pop()

                if not node.left and not node.right:
                    res += str(node.val) + "_"
                else:
                    if node.right:
                        stack.append(node.right)
                    if node.left:
                        stack.append(node.left)

            return res

        res1 = ""
        if root1:
            res1 = get_leaf_sequence(root1)

        res2 = ""
        if root2:
            res2 = get_leaf_sequence(root2)

        return res1 == res2
