from typing import Optional

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root:
            height_left = 0
            if root.left:
                left_node = root.left
                keep_going = True
                while keep_going:
                    height_left += 1
                    left_node = left_node.left
                    if left_node == None or left_node.left == None:
                        keep_going = False

            height_right = 0
            if root.right:
                right_node = root.right
                keep_going = True
                while keep_going:
                    height_right += 1
                    right_node = right_node.right
                    if right_node == None or right_node.right == None:
                        keep_going = False

            height_difference = abs(height_right - height_left)
            print(height_difference)
            if height_difference > 1:
                return False
            else:
                return (self.isBalanced(root.left) == True) and (self.isBalanced(root.right) == True)
        else:
            return True


if __name__ == '__main__':
    solution = Solution()

    nums = [-2,1,-3,4,-1,2,1,-5,4]
    output_1 = solution.maxSubArray(nums)
    expected_output = 6
    print(output_1)
