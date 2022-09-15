from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        stack = []
        stack.append((root, 0))

        palindrome_count = 0

        while stack:

            node, path = stack.pop()
            path = path ^ (1 << node.val)

            if not node.left and not node.right:
                if (path & (path - 1)) == 0:

                    palindrome_count += 1

            else:
                if node.left:
                    stack.append((node.left, path))

                if node.right:
                    stack.append((node.right, path))

        return palindrome_count

