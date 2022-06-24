import math
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBST_rec(root, {}, {})

    def isValidBST_rec(self, root: Optional[TreeNode], smallest_value_dic, largest_value_dic) -> bool:

        if not root:
            return True
        else:
            left_node = root.left
            right_node = root.right

            if left_node and right_node:

                if root.right in smallest_value_dic:
                    smallest_val_right = smallest_value_dic[root.right]
                else:
                    smallest_val_right = self.smallest_number(math.inf, root.right, smallest_value_dic)

                if root.left in largest_value_dic:
                    largest_va_left = largest_value_dic[root.left]
                else:
                    largest_va_left = self.largest_number(-math.inf, root.left, largest_value_dic)

                if largest_va_left < root.val and smallest_val_right > root.val:
                    return self.isValidBST(root.left, smallest_value_dic, largest_value_dic) & self.isValidBST(root.right, smallest_value_dic, largest_value_dic)
                else:
                    return False

            elif left_node:

                if root.left in largest_value_dic:
                    largest_va_left = largest_value_dic[root.left]
                else:
                    largest_va_left = self.largest_number(-math.inf, root.left, largest_value_dic)

                if largest_va_left < root.val:
                    return self.isValidBST(root.left)
                else:
                    return False

            elif right_node:

                if root.right in smallest_value_dic:
                    smallest_val_right = smallest_value_dic[root.right]
                else:
                    smallest_val_right = self.smallest_number(math.inf, root.right, smallest_value_dic)

                if smallest_val_right > root.val:
                    return self.isValidBST(root.right)
                else:
                    return False
            else:
                return True

    def smallest_number(self, input, root):
        if not root:
            return input
        else:
            input = min(input, root.val)
            return min(self.smallest_number(input, root.left), self.smallest_number(input, root.right))

    def largest_number(self, input, root):
        if not root:
            return input
        else:
            input = max(input, root.val)
            return max(self.largest_number(input, root.left), self.largest_number(input, root.right))




