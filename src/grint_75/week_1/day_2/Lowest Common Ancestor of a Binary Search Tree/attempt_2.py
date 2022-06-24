#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_value = p.val
        q_value = q.val

        val_root = root.val

        if p_value > val_root and q_value > val_root:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p_value < val_root and q_value < val_root:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root

if __name__ == '__main__':
    solution = Solution()

    nums = [-2,1,-3,4,-1,2,1,-5,4]
    output_1 = solution.maxSubArray(nums)
    expected_output = 6
    print(output_1)
