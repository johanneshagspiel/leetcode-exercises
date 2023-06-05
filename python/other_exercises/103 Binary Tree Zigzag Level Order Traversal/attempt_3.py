# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return root

        def dfs(node, level, level_list):

            if node:
                if level > len(level_list):
                    level_list.append(collections.deque())

                if level % 2 == 0:
                    level_list[level].append(node.val)
                else:
                    level_list[level].appendleft(node.val)

                if node.left or node.right:
                    dfs(node.left, level + 1, level_list)
                    dfs(node.right, level + 1, level_list)

                return level_list

        start_level_list = []
        start_level_list.append(collections.deque())

        return dfs(root, 0, start_level_list)
