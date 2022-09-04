import heapq
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []


        level_dic = {}

        stack = []
        stack.append((root, 0, 0))

        while stack:
            node, vertical_level, depth = stack.pop()

            if vertical_level not in level_dic:
                level_dic[vertical_level] = {}

            if depth not in level_dic[vertical_level]:
                level_dic[vertical_level][depth] = []

            level_dic[vertical_level][depth].append(node.val)

            if node.left:
                stack.append((node.left, vertical_level - 1, depth + 1))
            if node.right:
                stack.append((node.right, vertical_level + 1, depth + 1))

        priority_list = []

        for key, value in level_dic.items():
            priority_list.append((key, value))

        priority_list.sort(key= lambda x:x[0])

        result = []

        for vertical_level, depth_dic in priority_list:

            depth_priority_list = []
            for key, value in depth_dic.items():
                depth_priority_list.append((key, value))

            depth_priority_list.sort(key=lambda x: x[0])

            depth_list = []

            for depth, nodes in depth_priority_list:
                nodes.sort()
                depth_list.extend(nodes)

            result.append(depth_list)

        return result

