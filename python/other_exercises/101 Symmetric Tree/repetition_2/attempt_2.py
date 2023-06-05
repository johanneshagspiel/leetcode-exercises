# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        else:
            stack = []
            stack.append((root.left, root.right))

            while stack:
                left, right = stack.pop()

                if left and not right:
                    return False

                elif not left and right:
                    return False

                elif left and right:
                    if left.val != right.val:
                        return False
                    else:
                        stack.append((left.left, right.right))
                        stack.append((left.right, right.left))

            return True
