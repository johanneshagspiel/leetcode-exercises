from typing import Optional
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.isBalanced_Helper(root)[0]

    def isBalanced_Helper(self, root: Optional[TreeNode]) -> (bool, int):

        if not root:
            return True, -1

        left_balanced_boolean, left_height = self.isBalanced_Helper(root.left)
        if not left_balanced_boolean:
            return False, 0

        right_balanced_boolean, right_height = self.isBalanced_Helper(root.right)
        if not right_balanced_boolean:
            return False, 0

        height = 1 + max(left_height, right_height)
        balance_boolean = abs(left_height - right_height) < 2

        return balance_boolean, height


if __name__ == '__main__':
    solution = Solution()

    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    output_1 = solution.maxSubArray(nums)
    expected_output = 6
    print(output_1)
