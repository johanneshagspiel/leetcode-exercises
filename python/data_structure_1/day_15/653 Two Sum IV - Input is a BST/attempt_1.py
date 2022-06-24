from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        if not root:
            return False
        else:
            current_value = root.val

            remaining_value = k - current_value

            if remaining_value < current_value:
                correspondence = self.find_corresponding_value(root.left, remaining_value)
            else:
                correspondence = self.find_corresponding_value(root.right, remaining_value)

            if correspondence:
                return True
            else:
                return self.findTarget(root.left, k) or self.findTarget(root.right, k)


    def find_corresponding_value(self, root, needed_value):
        if not root:
            return False
        else:
            current_value = root.val
            remainder = needed_value - current_value

            if remainder == 0:
                return True
            elif remainder < 0:
                return self.find_corresponding_value(root.left, needed_value)
            else:
                return self.find_corresponding_value(root.right, needed_value)

