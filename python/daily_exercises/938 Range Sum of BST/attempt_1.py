# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        sum = 0

        if not root:
            return sum

        stack = [root]

        while stack:
            node = stack.pop()

            if low <= node.val <= high:
                sum += node.val

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return sum
