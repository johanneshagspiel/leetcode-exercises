from typing import Optional

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root == None:
            return True
        elif abs(self.height(root.left) - self.height(root.right)) > 1:
            return False
        else:
            return self.isBalanced(root.left) & self.isBalanced(root.right)


    def height(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        else:
            return 1 + max(self.height(root.left), self.height(root.right))


if __name__ == '__main__':
    solution = Solution()

    nums = [-2,1,-3,4,-1,2,1,-5,4]
    output_1 = solution.maxSubArray(nums)
    expected_output = 6
    print(output_1)
