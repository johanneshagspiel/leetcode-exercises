from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:

        def check_mode(current_value, prev_value):
            if current_value == (1 + prev_value):
                self.mode = "inc"
            elif current_value == (prev_value - 1):
                self.mode = "dec"
            else:
                self.mode = None


        tree_values = []

        def in_order_traversal(node):
            if node:
                in_order_traversal(node.left)
                tree_values.append(node.val)
                in_order_traversal(node.right)

        in_order_traversal(root)


        prev_value = tree_values[0]
        self.mode = None
        current_sequence = 1
        max_sequence = 1

        for value in tree_values[1:]:

            if not self.mode:
                check_mode(value, prev_value)
                if self.mode:
                    current_sequence += 1
                    prev_value = value

            else:
                if self.mode == "inc":
                    if value == (1 + prev_value):
                        current_sequence += 1
                        prev_value = value
                    else:
                        max_sequence = max(max_sequence, current_sequence)
                        current_sequence = 1
                        check_mode(value, prev_value)
                        if self.mode:
                            current_sequence += 1
                            prev_value = value
                else:
                    if value == (prev_value - 1):
                        current_sequence += 1
                        prev_value = value
                    else:
                        max_sequence = max(max_sequence, current_sequence)
                        current_sequence = 1
                        check_mode(value, prev_value)
                        if self.mode:
                            current_sequence += 1
                            prev_value = value

        max_sequence = max(max_sequence, current_sequence)

        return max_sequence
