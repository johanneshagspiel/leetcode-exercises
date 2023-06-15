# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        maxSum = -float("inf")
        resultLevel = 0

        level = 1

        queue = collections.deque()
        queue.append(root)

        while queue:

            queue_len = len(queue)
            curSum = 0

            for _ in range(queue_len):
                node = queue.popleft()
                curSum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if curSum > maxSum:
                maxSum = curSum
                resultLevel = level
            level += 1

        return resultLevel
