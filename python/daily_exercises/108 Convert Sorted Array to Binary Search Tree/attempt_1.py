from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def rec_build(left, right):

            if left == right:
                node = TreeNode(val=nums[left])
                return node

            elif left > right or right < left:
                return None

            else:
                mid = left + ((right - left) // 2)

                root = TreeNode(val=nums[mid])
                root.left = rec_build(left, mid - 1)
                root.right = rec_build(mid + 1, right)

                return root

        return rec_build(0, len(nums) - 1)

