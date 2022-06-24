#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        val_left = p.val
        val_right = q.val

        if val_left > val_right:
            val_left, val_right = val_right, val_left

        val_root = root.val

        if val_right >= val_root and val_left <= val_root:
            return root
        elif val_right < val_root:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)


if __name__ == '__main__':
    solution = Solution()

    nums = [-2,1,-3,4,-1,2,1,-5,4]
    output_1 = solution.maxSubArray(nums)
    expected_output = 6
    print(output_1)
