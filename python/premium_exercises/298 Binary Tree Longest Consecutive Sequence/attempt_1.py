# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        max_consecutive_len = 1

        stack = []
        stack.append((root, -float("inf"), 1))

        while stack:

            current_node, previous_value, previous_length = stack.pop()

            if current_node:
                if current_node.val - 1 == previous_value:
                    previous_length += 1
                else:
                    previous_length = 1

                max_consecutive_len = max(max_consecutive_len, previous_length)

                stack.append((current_node.left, current_node.val, previous_length))
                stack.append((current_node.right, current_node.val, previous_length))

        return max_consecutive_len
